import pygame
pygame.init()

class Pipe(pygame.sprite.Sprite):

    def __init__(self,isRotate,height):
        super().__init__()

        self.image = pygame.image.load('imgs/pipe.png').convert_alpha()
        self.image = pygame.transform.scale2x(self.image)

        if(isRotate):
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect(bottomleft=(400,-355))
        else:
            self.image = pygame.transform.scale(self.image,(self.image.get_width(),height))
            self.rect = self.image.get_rect(topleft=(400,285))


    
    def movement(self):
        self.rect.x -= 2

    def destroy(self):
        if(self.rect.x<=-80):
            self.kill()

    def update(self):
        self.destroy()
        self.movement()


