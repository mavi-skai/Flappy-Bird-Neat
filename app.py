import pygame
pygame.init()
from sys import exit
import random

def pipe_movement(pipe_list):
    print(len(pipe_list))
    if pipe_list:
        for pipe in pipe_list:
            pipe.x -= 4
            screen.blit(pipe_scale,pipe)

        pipe_list = [pipe for pipe in pipe_list if pipe.x > -85]
        return pipe_list
    else:
        return []

def pipe_collision(bird,pipe_list):
    if pipe_list:
        for pipe in pipe_list:
            if bird.colliderect(pipe):
                return False
    return True
    

width = 500
height = 670
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')  #set title 
pygame.display.set_icon(pygame.image.load('imgs/bird1.png')) #set icon
clock = pygame.time.Clock()
game_active = True

#background
background = pygame.image.load('imgs/bg.png').convert_alpha() # Load the image
background_scale = pygame.transform.scale(background,(width,height))

#ground
ground = pygame.image.load('imgs/ground.png').convert_alpha()
ground_scale =  pygame.transform.scale(ground,(width,100))

#fonts
font = pygame.font.Font('font/pixeltype.ttf',50) #create font
Generation = font.render('Generation: ',False,'Blue') #create surface for font
text_rect = Generation.get_rect(center = (50,30))

#bird
bird = pygame.image.load('imgs/bird1.png').convert_alpha()
bird_scale = pygame.transform.scale(bird,(bird.get_width()+10,bird.get_height() + 10))
bird_rect = bird_scale.get_rect(topleft = (200,300))
bird_gravity = 0.5

#pipe
pipe = pygame.image.load('imgs/pipe.png').convert_alpha()
pipe_scale = pygame.transform.scale(pipe,(80,200))
pipe_rect = pipe_scale.get_rect(topleft = (670,200))
pipe_list = []

#Timer
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,1000)

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
                pipe_list.append(pipe_scale.get_rect(topleft = (670,200)))
                print('summon pipe')
    
    if game_active:
        # Background, ground and fonts
        screen.blit(background_scale,(0,0)) #image , x,y
        screen.blit(ground_scale,(0,screen.get_height() - ground_scale.get_height()))
        screen.blit(Generation,text_rect)

        #pygame.draw.rect(screen,'Pink',bird_rect)

        #pipe
        pipe_list = pipe_movement(pipe_list)
        game_active = pipe_collision(bird_rect,pipe_list)

        #Bird gravity
        bird_gravity += 0.7
        bird_rect.y += bird_gravity
        if(bird_rect.bottom > screen.get_height() - ground_scale.get_height()):
            bird_rect.y = screen.get_height() - ground_scale.get_height() - bird_scale.get_height()
            
        screen.blit(bird_scale,bird_rect)

    
    # if(bird_rect.collidedict(pipe_rect)):  colliding to pipe
    #     pass
    

    pygame.display.update()
    clock.tick(60)   # Limit the frame rate to 60 FPS
    