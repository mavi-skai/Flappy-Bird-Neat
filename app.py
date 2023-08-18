import pygame
pygame.init()
from sys import exit
import random 
from pipe import Pipe
from bird import Bird
   
def collision_sprite():
    global game_active

    for bird in bird_group:
        bird_mask = pygame.mask.from_surface(bird.image)
        for pipe in pipe_group:
            pipe_mask = pygame.mask.from_surface(pipe.image)
            if bird_mask.overlap(pipe_mask, (pipe.rect.x - bird.rect.x, pipe.rect.y - bird.rect.y)):
                print('collide')
                game_active = False

#if(pygame.sprite.groupcollide(bird_group,pipe_group,False,False)):
#pygame.draw.rect(screen,'Pink',bird_rect)

width = 500
height = 670
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')  #set title 
pygame.display.set_icon(pygame.image.load('imgs/bird1.png')) #set icon
clock = pygame.time.Clock()
game_active = True

#Image load
background = pygame.image.load('imgs/bg.png').convert_alpha() # Load the image
ground = pygame.image.load('imgs/ground.png').convert_alpha()

#Scale
background_scale = pygame.transform.scale(background,(width,height))
ground_scale =  pygame.transform.scale(ground,(width,100))

#fonts
font = pygame.font.Font('font/pixeltype.ttf',50) #create font
Generation = font.render('Generation: ',False,'Blue') #create surface for font
text_rect = Generation.get_rect(center = (50,30))

#bird
bird_group = pygame.sprite.Group()
bird_group.add(Bird())

#pipe
pipe_group = pygame.sprite.Group()


#Timer
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,1700)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #to break while true

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_gravity = -11

            if event.type == pipe_timer:
                pipegap = 135
                pipe_height = random.randint(-100, 100)
                pipe_group.add(Pipe(False,(height//2)+pipe_height,pipegap))
                pipe_group.add(Pipe(True,(height//2)+pipe_height,pipegap))


    
    if game_active:
        #background
        screen.blit(background_scale,(0,0)) #image , x,y

        #pipe
        pipe_group.draw(screen) 
        pipe_group.update()

        #ground and fonts
        screen.blit(ground_scale,(0,screen.get_height() - ground_scale.get_height()))
        screen.blit(Generation,text_rect)

        #Bird gravity
        bird_group.draw(screen) 
        bird_group.update(screen) 

        #collision
        collision_sprite()
  
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)   # Limit the frame rate to 60 FPS
    