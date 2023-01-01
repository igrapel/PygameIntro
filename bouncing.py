import pygame, sys

pygame.init()

size = width, height = 900, 800
speed = [1,1]

col = 12, 233, 10

print(type(col))

screen =  pygame.display.set_mode(size)

#Get images for game
ball = pygame.image.load("ball.jpg")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
racket1 =  pygame.image.load("racket.jpg")
racket1 = pygame.transform.scale(racket1, (100, 100))
racketrect1 = racket1.get_rect(centerx = width/2)
racket2 =  pygame.image.load("racket.jpg")
racket2 = pygame.transform.scale(racket2, (100, 100))
racketrect2 = racket1.get_rect(centerx = width/2, y = screen.get_height() - 120)
goal1 = pygame.Rect(screen.get_width() / 2 - 73, 0, 175, 75)
goal2 = pygame.Rect(screen.get_width() / 2 - 73, screen.get_height()-75, 175, 75)

running = True
while(running):
    #To Close out
    for event in pygame.event.get():

        #check for arrow movement for racket 2
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_DOWN):
                racketrect2.y += 30
            elif(event.key == pygame.K_UP):
                racketrect2.y -= 30
            elif (event.key == pygame.K_RIGHT):
                racketrect2.x += 30
            elif (event.key == pygame.K_LEFT):
                racketrect2.x -= 30



        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0  or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Check for collision with racket 2
    if (racketrect1.colliderect(ballrect)):
        speed[0] = -speed[0]
        speed[1] = -speed[1]
    # Check for collision with racket 2
    if (racketrect2.colliderect(ballrect)):
        speed[0] = -speed[0]
        speed[1] = -speed[1]

    screen.fill(col)
    screen.blit(ball, ballrect)
    screen.blit(racket1, racketrect1)
    screen.blit(racket2, racketrect2)
    pygame.draw.rect(screen, (200, 120, 0), goal1)
    pygame.draw.rect(screen, (200, 120, 0), goal2)
    pygame.display.flip()
