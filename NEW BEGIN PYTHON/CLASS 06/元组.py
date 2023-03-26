import math
class circle:
    def __init__(self,r):
        self.r = r
    def getvolume(self):
        return 2*self.r*math.pi
b = circle(12)
print(b.getvolume())