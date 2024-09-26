import sys, pygame
import robot
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()

WIDTH, HEIGHT = 640, 640

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()            #get a pygame clock object
robotImage = pygame.image.load('Assets/logo42.png').convert()
robotImage = pygame.transform.scale(robotImage, (50, 50))

bot = robot.ROBOT(WIDTH/2, HEIGHT/2)
background = pygame.image.load('Assets/VURCSkills.png').convert()
background = pygame.transform.scale(background, (640, 640))
background = pygame.transform.rotate(background, 90)
screen.blit(background, (0, 0))


def getInput():
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        bot.angularSpeed = 140/FPS
    elif keys[K_RIGHT]:
        bot.angularSpeed = -140/FPS
    else:
        bot.angularSpeed = 0
    if keys[K_UP]:
        bot.linearSpeed = 200/FPS
    elif keys[K_DOWN]:
        bot.linearSpeed = -200/FPS
    else:
        bot.linearSpeed = 0
    bot.setSpeed(bot.linearSpeed, bot.angularSpeed)
    bot.addPose(bot.vx, bot.vy, bot.angularSpeed)
time = 0
while True:
    time += 1/FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    getInput()
    pygame.draw.circle(screen, "gray", (bot.getPose().x, bot.getPose().y), 15)
    pygame.draw.line(screen, "red", (bot.getPose().x, bot.getPose().y), (bot.getPose().x+bot.vx*5, bot.getPose().y+bot.vy*5), 5)

    #screen.blit(robot.image, robot.pos)
    pygame.display.update()
    clock.tick(FPS)