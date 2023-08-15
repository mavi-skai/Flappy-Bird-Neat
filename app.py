import pygame
pygame.init()
from sys import exit



width = 450
height = 670
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')  #set title 
pygame.display.set_icon(pygame.image.load('imgs/bird1.png')) #set icon
clock = pygame.time.Clock()

background = pygame.image.load('imgs/bg.png').convert_alpha() # Load the image
background_resized = pygame.transform.scale(background,(width,height))

ground = pygame.image.load('imgs/ground.png').convert_alpha()
ground_resized =  pygame.transform.scale(ground,(width,100))

test_font = pygame.font.Font('font/pixeltype.ttf',50) #create font
text_surface = test_font.render('Test: ',False,'Blue') #create surface for font
#bird
bird = pygame.image.load('imgs/bird1.png').convert_alpha()
bird_resized = pygame.transform.scale(bird,(bird.get_width()+10,bird.get_height() + 10))
bird_rect = bird_resized.get_rect(topleft = (200,300))
#gravity
bird_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #to break while true
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
                bird_gravity = -20

    # Draw the resized image 
    screen.blit(background_resized,(0,0)) #image , x,y
    screen.blit(ground_resized,(0,screen.get_height() - ground_resized.get_height()))
    screen.blit(text_surface,(50,0))

    #pygame.draw.rect(screen,'Pink',bird_rect)
    bird_gravity += 1
    bird_rect.y += bird_gravity
    if(bird_rect.bottom > screen.get_height() - ground_resized.get_height()):
        bird_rect.y = screen.get_height() - ground_resized.get_height() - bird_resized.get_height()
        
    screen.blit(bird_resized,bird_rect)

    
    # if(bird_rect.collidedict(pipe_rect)):  colliding to pipe
    #     pass



   

    

    pygame.display.update()
    clock.tick(60)   # Limit the frame rate to 60 FPS
    