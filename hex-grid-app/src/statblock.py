import pygame

class Statblock(pygame.sprite.Sprite):

    def __init__(self, position, image):
        super().__init__()
        self.image = pygame.image.load(f"src/assets/{image}.png")
        if self.image.get_width() > self.image.get_height():
            self.image = pygame.transform.scale(self.image, (750, 500))
        else:
            self.image = pygame.transform.scale(self.image, (400, 500))
        self.position = position
        self.rect = self.image.get_rect(topleft=position)
