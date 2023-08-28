import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.jumping = True
        self.bird_fly_1 = pygame.image.load('imgs/bird1.png').convert_alpha()
        self.bird_fly_2 = pygame.image.load('imgs/bird2.png').convert_alpha()
        self.bird_fly_3 = pygame.image.load('imgs/bird3.png').convert_alpha()
        self.bird_index = 0 #to increment sprite
        # Scale factor for the bird images
        scale_factor = 1.2 
        # Scale the bird images
        self.bird_fly_1 = pygame.transform.scale(self.bird_fly_1, 
                                                 (int(self.bird_fly_1.get_width() * scale_factor), 
                                                  int(self.bird_fly_1.get_height() * scale_factor)))
        self.bird_fly_2 = pygame.transform.scale(self.bird_fly_2, 
                                                 (int(self.bird_fly_2.get_width() * scale_factor), 
                                                  int(self.bird_fly_2.get_height() * scale_factor)))
        self.bird_fly_3 = pygame.transform.scale(self.bird_fly_3, 
                                                 (int(self.bird_fly_3.get_width() * scale_factor), 
                                                  int(self.bird_fly_3.get_height() * scale_factor)))
        
        self.bird_fly = [self.bird_fly_1,self.bird_fly_2,self.bird_fly_3] #array of sprite
        self.image = self.bird_fly[self.bird_index] #set sprite
        self.rect = self.image.get_rect(center = (200,300))
        self.bird_gravity = 0.5
        

    def bird_input(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_SPACE] and self.jumping == True):
            self.bird_gravity = -10
            self.jumping = False

        if not keys[pygame.K_SPACE]:
            self.jumping = True


    def destroy(self):
        if (self.rect.x<=-80):
            self.kill()

    def apply_gravity(self,screen):
        self.bird_gravity+=0.7
        self.rect.y += self.bird_gravity
        if(self.rect.bottom > screen.get_height() - 100):
            self.rect.y = screen.get_height() - 100 - self.image.get_height()

    def animation(self):
        self.bird_index+=0.1
        if(self.bird_index>len(self.bird_fly)):
            self.bird_index = 0
        self.image = self.bird_fly[int(self.bird_index)]
        
    def update(self,screen):
        self.animation()
        self.bird_input()
        self.apply_gravity(screen)