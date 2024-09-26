import math
from vector2d import V
import physics

class ROBOT:
    def __init__(self, x, y, FPS):
        self.object = physics.Object(1/FPS)
        self.object.pos = V[x, y]
        self.object.setDir(0)
    def setPose(self, x, y, theta):
        self.object.pos = V[x, y]
        self.object.setDir(math.radians(-90-theta))
    def addPose(self, x, y, theta):
        self.object.pos += V[x, y]
        self.object.setDir(self.object.dir().angle() + theta)
    def getPose(self):
        return self.pos
    def drive(self, pct):
        self.object.drive(pct)
    def update(self, lpct, apct):
        self.drive(lpct)

        self.object.setDir(self.object.dir().angle(V(1,0)) + apct)
        self.object.pos += self.object.getChange(lpct)