import math
import numpy as np

class Object:
    def __init__(self, dt):
        self.dt = dt
        self.weight = 15 * 0.453592 # kg
        self.maxTorque = 2 # Newton Meters
        self.wheelRadius = 2.75 * 0.0254 * 0.5 # meters
        self.maxRPM = 450
        self.muY = .9
        self.muX = .4
        self.dir = np.array([0, 0]) # angle in standard form radians
        self.vel = np.array([0, 0]) # local velocity
        self.acc = np.array([0, 0]) # local acceleration
        self.force = np.array([0, 0]) # local force
    def setDir(self, angle):
        self.dir = math.radians(-90-angle)
    def drive(self, pct):
        self.fn = self.weight * 9.8 
        self.fy = self.fn * self.muY
        self.fx = self.fn * self.muX
        self.forceY = ((self.maxTorque*pct) / self.wheelRadius) - self.fy
        self.acc[0] = self.forceY / self.weight
        self.acc[1] = self.fx / self.weight
        self.vel[0] += self.acc[0]

        if (abs(self.vel[0]) > self.maxRPM):
            self.vel[0] = self.maxRPM
        if (abs(self.vel[0]) < -self.maxRPM):
            self.vel[0] = -self.maxRPM


        if (abs(self.vel[0] > 0)):
            self.vel[0] -= self.acc[0]
        if (abs(self.vel[0] < 0)):
            self.vel[0] += self.acc[0]

        if (abs(self.vel[1] > 0)):
            self.vel[1] -= self.acc[1]
        if (abs(self.vel[1] < 0)):
            self.vel[1] += self.acc[1]
    def getChange(self, pct):
        self.drive(pct)
        dx = self.vel[0] * math.cos(self.dir) + self.vel[1] * math.sin(self.dir)
        dy = self.vel[0] * math.sin(self.dir) + self.vel[1] * math.cos(self.dir)
        return np.array([dx, dy])