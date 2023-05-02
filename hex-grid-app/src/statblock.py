import pygame

class Statblock(pygame.sprite.Sprite):
    def __init__(self, position, hexa, image):
        super().__init__()
        self.image = pygame.image.load(f"src/assets/{image}.png")
        self.hexa = hexa
        self.position = position
        self.rect = self.image.get_rect(topleft=position)


        
    
