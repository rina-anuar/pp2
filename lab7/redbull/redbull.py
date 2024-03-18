import pygame
import sys

pygame.init()
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Red ball')
clock = pygame.time.Clock()#заддержка жасайды 

x = 47  # initial pos of ball  
y = 47
r = 25
speed = 20
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
                keys = pygame.key.get_pressed()#клавишы которые были нажаты
                if keys[pygame.K_LEFT] and x-r-speed>=0: # если нажать влево
                              x = x-speed
                elif keys[pygame.K_RIGHT] and x+r+speed<=window_width: # если нажать вправо
                              x = x+speed
                if keys[pygame.K_UP] and y-r-speed>=0: # если нажать вврех
                              y = y-speed
                elif keys[pygame.K_DOWN] and y+r+speed<=window_height: # если нажать вниз
                              y = y+speed

        window.fill((255, 255, 255))  # white screen 

        pygame.draw.circle(window, 'red', (x, y), r)
        
        pygame.display.flip()#буферизация чтобы переворачивать экран (update тоже можно)
        clock.tick(120)
    

pygame.quit()