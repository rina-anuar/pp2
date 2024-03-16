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

    minute_angle = 360 - (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width())/2, (size[1] - min_rotate.get_width())/2)
    screen.blit(min_rotate, min_pos)

    second_angle = 360 - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width())/2, (size[1] - sec_rotate.get_width())/2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()