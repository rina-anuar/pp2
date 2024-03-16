import pygame, time
import sys 

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode((size))

back = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/back.jpg')
minutes = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/minutes.png')
seconds = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/seconds.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(back ,(0, 0))
    now = time.localtime()


    pygame.display.flip()

pygame.quit()
sys.exit()