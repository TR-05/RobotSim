WIDTH, HEIGHT = 640, 640
Scaler = WIDTH/144
def toPixels(x):
    return (int(x/144*WIDTH))
def toCoords(x):
    return (x/WIDTH * 144)

class obj:
    def __init__(self, x, y, speed, FPS):
        self.x = x
        self.y = y
        self.FPS = FPS
        self.speed = speed
        self.weight = 15 * 0.453592 # 15 lbs to kg
        self.mu = 0.1
    def move(self):
        sgn = 0
        if (self.speed != 0):
            sgn = self.speed / abs(self.speed)
        ff = 9.8 * self.weight * self.mu
        decel = (ff / self.weight) / self.FPS
        print(decel)
        if (abs(self.speed) > decel):
            self.speed -= decel
        else:
            self.speed = 0
        pixelSpeed = toPixels(self.speed * 0.0254) / self.FPS
        self.x += pixelSpeed
        self.y += pixelSpeed
        print(sgn)