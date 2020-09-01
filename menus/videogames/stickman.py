import sys,pygame

pygame.init()

background = pygame.image.load('background1.jpg')
size = (128,128)
background = pygame.transform.scale(background, size)
while 1:
    screen = pygame.display.set_mode(size)
    screen.blit(background,(0,0))
    pygame.display.update()