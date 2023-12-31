import pygame
pygame.init()

class Pipe(pygame.sprite.Sprite):

    def __init__(self,isRotate,height,pipegap):
        super().__init__()

        self.image = pygame.image.load('imgs/pipe.png').convert_alpha()

        if(isRotate):
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect(bottomleft=(670,height-(pipegap//2)))
        else:
            self.rect = self.image.get_rect(topleft=(670,height+(pipegap//2)))


    
    def movement(self):
        self.rect.x -= 2

    def destroy(self):
        if(self.rect.x<=-80):
            self.kill()

    def update(self):
        self.destroy()
        self.movement()


