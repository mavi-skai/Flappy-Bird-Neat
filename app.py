import pygame
pygame.init()
from sys import exit



width = 450
height = 670
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')  #set title 
pygame.display.set_icon(pygame.image.load('imgs/bird1.png')) #set icon
clock = pygame.time.Clock()

background = pygame.image.load('imgs/bg.png') # Load the image
resized_background = pygame.transform.scale(background,(width,height))

ground = pygame.image.load('imgs/ground.png')
resized_ground =  pygame.transform.scale(ground,(width,100))

test_font = pygame.font.Font('font/pixeltype.ttf',50) #create font
text_surface = test_font.render('Test: ',False,'Blue') #create surface for font



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           
            exit()  #to break while true

    # Draw the resized image 
    screen.blit(resized_background,(0,0)) #image , x,y
    screen.blit(resized_ground,(0,screen.get_height() - resized_ground.get_height()))
    screen.blit(text_surface,(50,0))
    pygame.display.update()
    clock.tick(60)   # Limit the frame rate to 60 FPS
    