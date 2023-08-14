import pygame
pygame.init()
from sys import exit



width = 800
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird') #set title 
pygame.display.set_icon(pygame.image.load('./imgs/bird1.png')) #set icon


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #to break while true
        
    pygame.display.update()
    