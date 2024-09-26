import math
import pose

class ROBOT:
    def __init__(self, x, y):
        self.linearSpeed = 0
        self.angularSpeed = 0
        self.vx = 0
        self.vy = 0
        self.pose = pose.POSE(x, y, 0)
        self.thetaRad = 0
    def setPose(self, x, y, theta):
        self.pose.x = x
        self.pose.y = y
        self.pose.theta = theta
        self.thetaRad = math.radians(-90-theta)
    def addPose(self, x, y, theta):
        self.pose.x += x
        self.pose.y += y
        self.pose.theta += theta
        self.thetaRad = math.radians(-90-theta)
    def setSpeed(self, linearSpeed, angularSpeed):
        self.linearSpeed = linearSpeed
        self.angularSpeed = angularSpeed
        self.thetaRad = math.radians(-90-self.pose.theta)
        self.vx = linearSpeed * math.cos(self.thetaRad)
        self.vy = linearSpeed * math.sin(self.thetaRad)
    def getPose(self):
        return self.pose
