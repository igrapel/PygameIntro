import pygame
pygame.init()

screen = pygame.display.set_mode([700, 800])

running = True
ball = pygame.image.load("ball.jpg")
ball_img = ball.get_rect()

while(running):
    screen.fill((100, 0, 10))
    screen.blit(ball, ball_img)
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            running = False


    pygame.draw.circle(screen, (0, 0, 200), (245, 245), 75)