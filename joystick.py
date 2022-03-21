# class dealing with handing joystick inputs
# what should it handle?
# - set center
# - determine X and Y direction based on supplied coordinates

class Joystick:
    def __init__(self, deadZone, xCenter, yCenter, xIncrement, yIncrement):
        self.deadZone = deadZone
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xIncrement = xIncrement
        self.yIncrement = yIncrement
        
    # gets new center coordinates
    def Center(self, centerX, centerY):
        self.xCenter = centerX
        self.yCenter = centerY
        
    # determines the increment to the X coordinate
    def CheckX(self, xCoord):
        if (xCoord > self.xCenter + self.deadZone):
            return self.xIncrement
        if (xCoord < self.xCenter - self.deadZone):
            return -self.increment
        
        return 0
    
    # determines the increment to the Y coordinate
    def CheckY(self, yCoord):
        if (yCoord > self.yCenter + self.deadZone):
            return self.yIncrement
        if (yCoord < self.yCenter - self.deadZone):
            return -self.yIncrement
        
        return 0