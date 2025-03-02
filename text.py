import pygame
pygame.init()
from globals import *

class TextEntity(pygame.sprite.Sprite):
    def __init__(self, groups, surface = pygame.Surface((100, 100)), position = (0, 0), font = pygame.font.SysFont('Arial', 64), color=pygame.Color('black')):     # groups used to categorize sprites (e.g. visibile sprite, invisibile sprite, etc.) pNOTE SAME AS SPRITE BUT USES SURFACE INSTEAD OF IMAGE
        #super().__init__(groups)
        self.color = color
        #self.surface = surface
        #self.rect = self.image.get_rect(topleft = position)

    # def update(self):
    #     self.rect.x += 1

    def blit_text(self, surface, position, font, color, text):
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0] # Reset he x
                    y += word_height # Start on new row
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0] # Reset x
            y += word_height # Start on new row

    # def blit_text(self, groups, surface, position, font, color, text):
    #     words = [word.split(' ') for word in text.splitlines()]
    #     space = font.size(' ')[0]
    #     max_width, max_height = surface.get_size()
    #     x, y = position
    #     for line in words:
    #         for word in line:
    #             word_surface = font.render(word, 0, color)
    #             word_width, word_height = word_surface.get_size()
    #             if x + word_width >= max_width:
    #                 x = position[0] # Reset he x
    #                 y += word_height # Start on new row
    #             surface.blit(word_surface, (x, y))
    #             x += word_width + space
    #         x = position[0] # Reset x
    #         y += word_height # Start on new row


