import random
from paddle import Paddle

# class representing a computer paddle
# inherits from paddle.py
class ComputerPaddle(Paddle):
    def __init__(self, x, y, width, height, paddleName, distance, percentage):
        super().__init__(x, y, width, height, paddleName)
        self.distance = distance
        self.percentage = percentage

    # moves the paddle based on supplied values
    # Additional code to handle how close the ball is to the paddle before it 
    #  can move and what percentage the computer paddle will respond once the 
    #  ball is in range.
    def MovePaddle(self, yIncrement, minY, maxY, ballX, ballY):
        # computer paddle movement doesn't occur until the ball is a specified distance
        # or less from the paddle and only for a specified percentage
        
        #self.y += yIncrement
        #      
        #if (self.UpperLeftY() <= minY):
        #    self.y = minY + int((self.height - 1) / 2)
        #if (self.LowerRightY() >= maxY):
        #    self.y = maxY - int((self.height - 1) / 2)
            
        if (self.UpperLeftX() - ballX <= self.distance):
            # updated rule - computer will only respond to the ball if it
            # within a specified distance of the paddle a specified percentage
            # of the time.
            if (random.randint(1, 100) <= self.percentage):
                if (ballY > self.y):
                    super().MovePaddle(yIncrement, minY, maxY)
                if (ballY < self.y):
                    super().MovePaddle(-yIncrement, minY, maxY)