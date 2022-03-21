import random
from paddle import Paddle

class Ball:
    # initialize class
    def __init__(self, x, y, directionX, directionY, size):
        self.x = x
        self.y = y
        self.directionX = directionX
        self.directionY = directionY
        self.size = size
        
        # the size of the ball should be an odd number
        # so that there is an actual center
        if (self.size % 2 == 0):
            self.size += 1
        
    # moves the ball on the playfield, adjusts direction as needed
    # returns: -1 if X is at left side, 0 otherwise
    def MoveBall(self, minX, maxX, minY, maxY):
        self.x += self.directionX
        self.y += self.directionY
        
        # check if the ball hit the right sides
        # if (self.x == minX or self.x == maxX):
        #     self.directionX = -self.directionX
        if (self.LowerRightX() >= maxX):
            self.directionX = -self.directionX
        
        # check if the ball hit the top or bottom sides
        if (self.UpperLeftY() <= minY or self.LowerRightY() >= maxY):
            self.directionY = -self.directionY
        
        if (self.UpperLeftX() <= minX):
            return -1
        if (self.LowerRightX() >= maxX):
            return -2
        
    def MoveBall2(self, minX, maxX, minY, maxY, paddle, checkLeft):
        self.x += self.directionX
        self.y += self.directionY
        
        # check if the ball hit the right sides
        # if (self.x == minX or self.x == maxX):
        #     self.directionX = -self.directionX
        if (self.LowerRightX() >= maxX):
            self.directionX = -self.directionX
        
        # check if the ball hit the top or bottom sides
        if (self.UpperLeftY() <= minY or self.LowerRightY() >= maxY):
            self.directionY = -self.directionY
        
        # check if the ball hit the paddle
        if (checkLeft):
            if (self.UpperLeftX() == paddle.LowerRightX()):
                if ((self.UpperLeftY() >= (paddle.UpperLeftY() - 1) and (self.LowerRightY() <= (paddle.LowerRightY() + 1)))):
                    self.directionX = -self.directionX
        else:                    
            if (self.LowerRightX() == paddle.UpperLeftX()):
                if ((self.UpperLeftY() >= (paddle.UpperLeftY() - 1) and (self.LowerRightY() <= (paddle.LowerRightY() + 1)))):
                    self.directionX = -self.directionX
                    
        # check if the ball reached the left or right side
        if (self.UpperLeftX() <= minX):
            return -1
        if (self.LowerRightX() >= maxX):
            return -2
        
        return 0
            
    # randomly determines horizontal and vertical movement
    def InitializeBallDirection(self):
        # ball direction can either be -1 or 1
        # if 0 the ball wouldn't move in that particular direction
        while (self.directionX != 1 and self.directionX != -1):
            self.directionX = random.randint(-1, 1)
        
        while (self.directionY != 1 and self.directionY != -1):
            self.directionY = random.randint(-1, 1)
    
    # determine where the ball will start
    def InitializeBallLocation(self):
        # ball should start within the following area:
        # (80, 5) - (127, 57)
        # range of 48, 52
        # 3/8/2022 - ball should start in the horizontal center of the display
        # self.x = 80 + random.randint(0, 47)
        # self.y = 5 + random.randint(0, 52)
        self.x = 63
        self.y = 5 + random.randint(0, 52)
        
    # these defs get the calculated upper-left and lower-right coordinates of the ball
    def UpperLeftX(self):
        return self.x - int((self.size - 1) / 2)
    def UpperLeftY(self):
        return self.y - int((self.size - 1) / 2)
    def LowerRightX(self):
        return self.x + int((self.size - 1) / 2)
    def LowerRightY(self):
        return self.y + int((self.size - 1) / 2)
    