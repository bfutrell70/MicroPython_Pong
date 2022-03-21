from machine import Pin, SoftI2C, ADC
import ssd1306
import time
import machine
import random

from ball import Ball
from paddle import Paddle
from joystick import Joystick
from computer_paddle import ComputerPaddle

# set frequency to 240 mhz
machine.freq(240000000)

# delay between loop iterations
timeDelay = 0.01

# set up OLED display using default address 0x3c
i2c = SoftI2C(sda = Pin(25), scl = Pin(26))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# ball object
# x, y, direction x, direction y, ball size
ball = Ball(1, 0, 0, 0, 3)

# joystick object
# deadZone, xCenter, yCenter, xIncrement, yIncrement
increment = 2
deadZone = 150
joystick = Joystick(deadZone, 0, 0, increment, increment)

# number of games played, maximum number of games to play
game = 0
maxGames = 10

# dimensions of paddle
paddleWidth = 3
paddleHeight = 11

# this was done as a test to allow me to let the program run without intervention
# to see if the no ball issue appears
playerPaddleHeight = 11

# ball distance from the computer paddle before it reacts
computerReactDistance = 40

# chance of computer reacting to the ball once it is in range
computerReactionChance = 70

# set up paddles (player and computer)
# X, Y, width, height, player name
paddle = Paddle(0, int((64 - playerPaddleHeight) / 2), paddleWidth, playerPaddleHeight, "player")
# X, Y, width, height, player name, reaction distance before the paddle responds to the ball, percentage that the paddle will respond to the ball
computerPaddle = ComputerPaddle(127, int((64 - paddleHeight) / 2), paddleWidth, paddleHeight, "computer", computerReactDistance, computerReactionChance)

# set up I/O pins for joystick
xVal = ADC(Pin(39))
yVal = ADC(Pin(36))
zVal = Pin(17, Pin.IN, Pin.PULL_UP)

xVal.atten(ADC.ATTN_11DB)
yVal.atten(ADC.ATTN_11DB)
xVal.width(ADC.WIDTH_12BIT)
yVal.width(ADC.WIDTH_12BIT)

# ------ START OF FUNCTIONS ------
   
# draw the playield
def DrawPlayfield():
    global display
    
    # top line
    display.hline(0, 0, 128, 1)
    
    # bottom line
    display.hline(0, 63, 128, 1)
    
    # line on opposite side of player's paddle
    # not needed now that there is a computer player
    #display.vline(127, 0, 64, 1)
    
# draw the paddle
def DrawPaddles():
    global paddle, computerPaddle
    
    # x, y, width, height
    display.fill_rect(
        paddle.UpperLeftX(),
        paddle.UpperLeftY(),
        paddle.width,
        paddle.height, 1)
    
    display.fill_rect(
        computerPaddle.UpperLeftX(),
        computerPaddle.UpperLeftY(),
        computerPaddle.width,
        computerPaddle.height, 1)

# draws the ball on the display
def DrawBall():
    global ball
    
    display.fill_rect(ball.UpperLeftX(), ball.UpperLeftY(), ball.size, ball.size, 1)    

# draws a message that the ball was missed
def DrawMissedBall():
    display.fill(0)
    display.text('Missed it by', 0, 10, 1)
    display.text('THAT much...', 0, 20, 1)
    display.show()
    time.sleep(3)
    
def DrawComputerMissedBall():
    display.fill(0)
    display.text('The COMPUTER', 0, 10, 1)
    display.text('missed it by', 0, 20, 1)
    display.text('THAT much...', 0, 30, 1)
    display.show()
    time.sleep(3)
    
def Reset():
    global paddle, ball, display, game, maxGames, joystick

    game += 1
    
    if (game > maxGames):
        # print("drawing thanks for playing text")
        display.fill(0)
        display.text('Thanks for', 0, 0, 1)
        display.text(f'playing {maxGames} rounds!', 0, 10, 1)
        display.show()
    else:
        # pause before starting the loop
        display.fill(0)
        display.text('Waiting 5 sec.', 0, 0, 1)
        display.text('Before starting', 0, 10, 1)
        display.text(f'round {game}!', 0, 20, 1)
        
        if (game == 1):
            # get values of joystick when centered
            # this will accomodate using this program
            # on different boards and joysticks
            # ----------------------
            joystick.Center(xVal.read(), yVal.read())
            
            display.hline(0, 35, 128, 1)
            display.text("Keep joystick", 0, 40, 1)
            display.text("centered.....", 0, 50, 1)
        
        display.show()
        time.sleep(5.0)
        
        # height of display?
        paddle.Reset(64)
        
        ball.InitializeBallLocation()
        ball.InitializeBallDirection()    
        
# ------ END OF FUNCTIONS ------

Reset()

# main loop
while True:
    if (game <= maxGames):
        x = xVal.read()
        y = yVal.read()
        z = zVal.value()
                
        paddle.MovePaddle(joystick.CheckY(y), 1, 62)
        
        computerPaddle.MovePaddle(increment, 1, 62, ball.x, ball.y)
        
        # clear the display
        display.fill(0)
        
        DrawPlayfield()
        DrawPaddles()
        
        # minX, maxX, minY, maxY
        ballValue = ball.MoveBall(1, 127, 1, 62)
        print(f'ballValue: {ballValue}')
               
        # ***** Check if the ball hit the paddle *****
        # if the left side of the ball is the same as the left side of the paddle + width
        # and (the top of the ball is equal to or greater than the top of the paddle - 1
        # or the bottom of the ball is equal to or less than the bottom of the paddle + 1)
        # then change the X direction
        # NOTE: This condition should be moved to the Ball class.
        if (ball.UpperLeftX() == (paddle.UpperLeftX() + paddle.width)):
            if ((ball.UpperLeftY() >= (paddle.UpperLeftY() - 1) and (ball.LowerRightY() <= (paddle.LowerRightY() + 1)))):
                ball.directionX = -ball.directionX
                
        # check if the ball passed the player's paddle
        if (ballValue == -1):
            DrawMissedBall()
            Reset()
        
        # check if the ball passed the computer's paddle
        if (ballValue == -2):
            DrawComputerMissedBall()
            Reset()
        
        # check if the ball has hit the computer paddle
        if (ball.UpperLeftX() == (computerPaddle.UpperLeftX())):
            if ((ball.UpperLeftY() >= (computerPaddle.UpperLeftY() - 1) and (ball.LowerRightY() <= (computerPaddle.LowerRightY() + 1)))):
                ball.directionX = -ball.directionX
        
        # print('drawing the ball')
        DrawBall()
        
        display.show()
        time.sleep(timeDelay)
