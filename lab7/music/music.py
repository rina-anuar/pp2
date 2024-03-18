import pygame, time
import sys 

pygame.init()
size = (1500, 2000)
screen = pygame.display.set_mode((size))

player = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/music/img/1.jpeg')
player1 = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/music/img/2.jpeg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(player ,(0, 0))
    
    
    pygame.display.flip()

pygame.quit()
sys.exit()