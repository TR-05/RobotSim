import math
import numpy as np
import vector2d as v2d
class Object:
    def __init__(self, dt):
        self.dt = dt
        self.weight = 15 * 0.453592 # kg
        self.maxTorque = 2 # Newton Meters
        self.wheelRadius = 2.75 * 0.0254 * 0.5 # meters
        self.maxRPM = 450
        self.muY = .9
        self.muX = .4
        self.dir = v2d.V(0,0) # robot forward direction
        self.vel = v2d.V(0,0) # global velocity
        self.acc = v2d.V(0,0) # local acceleration
        self.force = v2d.V(0,0) # local force
        self.pos = v2d.V(0,0) # global position
    def setDir(self, angle):
        self.dir = v2d.V(math.cos(math.radians(-90-angle)), math.sin(math.radians(-90-angle)))
    def drive(self, pct):
        self.fn = self.weight * 9.8 
        self.fy = self.fn * self.muY
        self.fx = self.fn * self.muX

        # get the signed magnitude of the drive motor force - force of friction opposing
        sgn = 1
        if pct == 0:
            sgn = 1
        else:
            sgn = pct/abs(pct)
        self.forceYscaler = (abs(((self.maxTorque*(pct/100.0)) / self.wheelRadius)) - self.fy) * sgn
        self.force = self.dir.unit() * self.forceYscaler
        self.acc = self.force / self.weight
        self.vel += self.acc

    def getChange(self, pct):
        self.drive(pct)
        dx = self.vel[0] * math.cos(self.dir) + self.vel[1] * math.sin(self.dir)
        dy = self.vel[0] * math.sin(self.dir) + self.vel[1] * math.cos(self.dir)
        return v2d.V(dx, dy)