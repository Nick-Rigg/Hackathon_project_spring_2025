import pygame
from globals import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((100, 100)), position = (0, 0)):     # groups used to categorize sprites (e.g. visibile sprite, invisibile sprite, etc.)
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        #self.rect.x += 1
        pass


# class SuperEntity(Entity):
#     def __init__(self, groups, image = pygame.Surface((100, 100)), position = (0, 0)):     # groups used to categorize sprites (e.g. visibile sprite, invisibile sprite, etc.)
#         super().__init__(groups)

#     def update(self):
#         #return super().update()
#         self.rect.y += 1