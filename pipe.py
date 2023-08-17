import pygame
pygame.init()

class Pipe(pygame.sprite.Sprite):

    def __init__(self,height,isRotate):
        super().__init__()

        self.image = pygame.image.load('imgs/pipe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, height))

        if(isRotate):
            self.image = pygame.transform.rotate(self.image, 180) 
            self.rect = self.image.get_rect(midtop=(400,0))
        else:
            self.rect = self.image.get_rect(midbottom=(400,570))


    
    def movement(self):
        self.rect.x -= 2

    def destroy(self):
        if(self.rect.x<=-80):
            self.kill()

    def update(self):
        self.destroy()
        self.movement()


