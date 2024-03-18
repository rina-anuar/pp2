import pygame, time
import sys 

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode((size))
pygame.display.set_caption('mickey mouse clock')

back = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/back.jpg')
minutes = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/minutes.png')
seconds = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/seconds.png')
#hours = pygame.image.load('/Users/rinaanuar/Desktop/pp2/pp2/lab7/clock/hours.png')

while True:#infinite loop for show pygame window on the screen 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()#when you press the button esc(x) the window will close

    screen.blit(back ,(0, 0))
    now = time.localtime()
    
    min_angle = 360 - (now.tm_min*6)#для вычисления угла поворота минутной стрелки
    min_rot = pygame.transform.rotate(minutes, min_angle)#rotate min 
    min_pos = ((size[0]-min_rot.get_width())/2, (size[1]-min_rot.get_width())/2)#bir narsenin sentirde turganyn korsetu ushin size dan sol narsenin uzyndygyn alyp ekige bolemiz 
    screen.blit(min_rot, min_pos)
     
    sec_angl = 360 - (now.tm_sec*6)
    sec_rot = pygame.transform.rotate(seconds, sec_angl)
    sec_pos = ((size[0]-sec_rot.get_width())/2, (size[1]-sec_rot.get_width())/2)
    screen.blit(sec_rot, sec_pos)

    '''hour_angle = 360 - ((now.tm_hour % 12 + now.tm_min / 60) * 30) # 30 градусов на каждый час
    hour_rot = pygame.transform.rotate(hours, hour_angle)
    hour_pos = ((size[0] - hour_rot.get_width()) / 2, (size[1] - hour_rot.get_height()) / 2)
    screen.blit(hour_rot, hour_pos)'''

    
    pygame.display.flip()

pygame.quit()
sys.exit()