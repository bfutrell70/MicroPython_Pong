class Paddle:
    def __init__(self, x, y, width, height, paddleName):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.paddleName = paddleName
                
        # the height of the paddle should be an odd number
        # so that there is an actual center
        if (self.height % 2 == 0):
            self.height += 1
        
    # moves the paddle based on supplied values
    def MovePaddle(self, yIncrement, minY, maxY):
        self.y += yIncrement
              
        if (self.UpperLeftY() <= minY):
            self.y = minY + int((self.height - 1) / 2)
        if (self.LowerRightY() >= maxY):
            self.y = maxY - int((self.height - 1) / 2)
            
        #if (self.paddleName == "player"):
        #    print(f'---- paddle x: {self.x}')
        #    print(f'---- paddle y: {self.y}')
    
    # resets the paddle position
    def Reset(self, height):
        self.y = height - int((self.height) / 2)
    
    # these defs get the calculated upper-left and lower-right coordinates of the paddle
    def UpperLeftX(self):
        return self.x - int((self.width - 1) / 2)
    def UpperLeftY(self):
        return self.y - int((self.height - 1) / 2)
    def LowerRightX(self):
        return self.x + int((self.width - 1) / 2)
    def LowerRightY(self):
        return self.y + int((self.height - 1) / 2)