import pygame, sys

pygame.init()

size = width, height = 900, 800
speed = [3,2]

col = 200, 50, 10

print(type(col))

screen =  pygame.display.set_mode(size)

ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()

running = True
while(running):
    #To Close out
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0  or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(col)
    screen.blit(ball, ballrect)
    pygame.display.flip()