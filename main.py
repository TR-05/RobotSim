import sys, pygame
import math
pygame.init()

WIDTH, HEIGHT = 640, 640

FPS = 60

class GameObject:
    def __init__(self, image, speed, x, y):
        self.speed = speed
        self.original_image = image
        self.image = image
        self.pos = image.get_rect().move(x, y)
        self.theta = 0
    def setPos(self, x, y, theta):
        self.image = pygame.transform.rotate(self.original_image, theta)
        self.theta = theta
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos.x = x - self.width/2
        self.pos.y = y - self.height/2
        self.pos = self.image.get_rect(center=self.pos.center)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()            #get a pygame clock object
robotImage = pygame.image.load('Assets/logo4.png').convert()
robotImage = pygame.transform.scale(robotImage, (50, 50))

robot = GameObject(robotImage, 1, WIDTH/2, HEIGHT/2)
background = pygame.image.load('Assets/VURCSkills.png').convert()
background = pygame.transform.scale(background, (640, 640))
background = pygame.transform.rotate(background, 90)
screen.blit(background, (0, 0))

time = 0
def updatePos(t):
    s = 200
    robot.setPos(WIDTH/2 + s*math.cos(t), HEIGHT/2 + s*math.sin(t), 360*t)
    
while True:
    time += 1/FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, robot.pos, robot.pos)
    updatePos(time)
    screen.blit(robot.image, robot.pos)
    pygame.display.update()
    clock.tick(FPS)