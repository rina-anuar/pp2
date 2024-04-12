#Imports
import pygame, sys, random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (400, 600)
SPEED, USER_SPEED = 7, 5
SCORE, MONEY = 0, 0
PAUSE, END = False, False
y = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
name = font.render("Street racer", True, BLACK)

#Loading needed images
background = pygame.image.load("AnimatedStreet.png")
coin = pygame.image.load("coin.png")
enemy = pygame.image.load("Enemy.png")
player = pygame.image.load("Player.png")
#road = pygame.image.load("Road.png")
dollar = pygame.image.load("rubin.png")

#Loading background music
#background_music = pygame.mixer.music.load("sounds/Sueta.mp3")
#pygame.mixer.music.set_volume(0.2)

#Create a green screen and show game splash screen
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
DISPLAYSURF.fill(GREEN)
DISPLAYSURF.blit(name, (15, 150))
pygame.display.set_caption("Street Racer")
pygame.display.update()
time.sleep(2)


class Timer:
    def __init__(self):
        self.start_time = 0
        self.time_in_pause = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        self.time_in_pause = self.elapsed_time
 
    def unpause(self):
        self.start_time = time.time()
        
    def current_time(self):
        self.elapsed_time = round(time.time() - self.start_time + self.time_in_pause, 2)
        game_time = font_small.render("time: " + str(self.elapsed_time), True, BLACK)
        DISPLAYSURF.blit(game_time, (10, 140))

    def restart(self):
        self.__init__()
        self.start()

    def end(self):
        game_end_time = font_small.render("Seconds: " + str(self.elapsed_time), True, BLACK)
        DISPLAYSURF.blit(game_end_time, (30, 300))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, 385), -50)

    def change_location(self):
        self.rect.center = (random.randint(15, 385), -50)

    def move(self):
        self.rect.move_ip(0, USER_SPEED)
        if self.rect.top > 600: self.change_location()

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

class Dollar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dollar
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.change_location()

    def change_location(self):
        self.rect.center = (random.randint(15, 385), -3000)

    def move(self):
        self.rect.move_ip(0, USER_SPEED)
        if self.rect.top > 600: self.change_location()

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), -50)
    
    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            if SCORE % 10 == 0 and SCORE > 0:
                SPEED += 1
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), -50)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > USER_SPEED:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-USER_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH - USER_SPEED:        
            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(USER_SPEED, 0)
        if self.rect.top > USER_SPEED:
            if pressed_keys[pygame.K_w]:
                self.rect.move_ip(0, -USER_SPEED)
        if self.rect.bottom < SCREEN_HEIGHT - USER_SPEED:        
            if pressed_keys[pygame.K_s]:
                self.rect.move_ip(0, USER_SPEED)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)
              
#Setting up Sprites
P1 = Player()
E1 = Enemy()
M1 = Coin()
D1 = Dollar()

#Creating Timer object
T1 = Timer()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
all_sprites.add(D1)
moneys = pygame.sprite.Group()
moneys.add(M1)
moneys.add(D1)

#Playing the background music
#pygame.mixer.music.play(-1)

#Starting point of our game time
T1.start()

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if PAUSE:
                T1.unpause()
                #pygame.mixer.music.unpause()
                PAUSE = False
            else:
                T1.pause()
                #pygame.mixer.music.pause()
                PAUSE = True
                
        #Restart the game and initialize main variables and functions
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            for entity in all_sprites:
                entity.__init__() 
            SCORE, MONEY = 0, 0
            SPEED, USER_SPEED = 7, 5
            PAUSE, END = False, False
            y = 0
            T1.restart()
            #pygame.mixer.music.play(-1)
        
    #Check game state     
    if END or PAUSE: 
        
        pass

    else:    
    
        #Road animation
        y %= SCREEN_HEIGHT  
        DISPLAYSURF.blit(background, (0, y - SCREEN_HEIGHT))   
        if y < SCREEN_HEIGHT:
            DISPLAYSURF.blit(background, (0, y))
        y += USER_SPEED    

        scores = font_small.render(str(SCORE), True, BLACK)
        money_scores = font_small.render(str(MONEY), True, BLACK)
        current_speed = font_small.render("Your speed: " + str(USER_SPEED), True, BLACK)
        enemy_speed = font_small.render("Enemy speed: " + str(SPEED), True, BLACK)

        DISPLAYSURF.blit(scores, (10, 10))
        DISPLAYSURF.blit(money_scores, (365, 10))
        DISPLAYSURF.blit(current_speed, (10, 50))
        DISPLAYSURF.blit(enemy_speed, (10, 90))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            entity.move()
            entity.draw()
        
        #здесь надо закомментить
        collide_list = pygame.sprite.spritecollide(P1, moneys, False)
        
        #Check collision and change coordinates of the coin randomly   
        for object in collide_list:
            if object == M1:
                MONEY += 1
                #pygame.mixer.Sound('sounds/MarioCoinSound.mp3').play()
                M1.change_location()

            elif object == D1:
                MONEY += 3
                #pygame.mixer.Sound("sounds/yeahoo.mp3").play()
                D1.change_location()
            
        if MONEY % 10 == 0 and MONEY > 0: USER_SPEED += 1

        #To display current time on the screen   
        T1.current_time()

        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):  

            END = True

           # pygame.mixer.music.stop()
            #pygame.mixer.Sound('sounds/crash.wav').play()
            time.sleep(1)

            scores = font_small.render("Your Score: " + str(SCORE), True, BLACK)
            money_scores = font_small.render("Your Money: " + str(MONEY), True, BLACK)
            
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 150)) 
            DISPLAYSURF.blit(scores, (30, 350))
            DISPLAYSURF.blit(money_scores, (30, 400))
            T1.end()
            
            pygame.display.update()
                
        pygame.display.update()
        FramePerSec.tick(FPS)