import sys, pygame
#import robot
import vector2d as v2d
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from slowDown import obj
pygame.init()

WIDTH, HEIGHT = 640, 640
def toPixels(x, y):
    return (int(x/144*WIDTH), int(y/144*HEIGHT))
def toCoords(x, y):
    return (x/WIDTH * 144, y/HEIGHT * 144)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()            #get a pygame clock object
robotImage = pygame.image.load('Assets/logo42.png').convert()
robotImage = pygame.transform.scale(robotImage, (50, 50))

#bot = robot.ROBOT(WIDTH/2, HEIGHT/2, FPS)
background = pygame.image.load('Assets/VURCSkills.png').convert()
background = pygame.transform.scale(background, (640, 640))
background = pygame.transform.rotate(background, 90)
screen.blit(background, (0, 0))

thing = obj(WIDTH/2, HEIGHT/2, 6, FPS)
def getInput():
    keys=pygame.key.get_pressed()
    lpct = 0
    apct = 0
    if keys[K_LEFT]:
        apct = 140/FPS
    elif keys[K_RIGHT]:
        apct = -140/FPS
    else:
        lpct = 0
    if keys[K_UP]:
        lpct = 100
    elif keys[K_DOWN]:
        lpct = -100
    else:
        lpct = 0
    #bot.update(lpct, apct)
time = 0
while True:
    time += 1/FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    getInput()
    thing.move()
    pygame.draw.circle(screen, "gray", (thing.x, thing.y), 15)
    #pygame.draw.line(screen, "red", (bot.getPose().x, bot.getPose().y), (bot.getPose().x+bot.vx*5, bot.getPose().y+bot.vy*5), 5)

    #screen.blit(robot.image, robot.pos)
    pygame.display.update()
    clock.tick(FPS)