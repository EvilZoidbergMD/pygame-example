import pygame
import os

class SpriteSheet:
    
    def __init__(self, path_to_spritesheet, num_frames, dimensions, scaled_dimensions=(0,0)):
        self.width, self.height = dimensions
        self.s_width, self.s_height = scaled_dimensions

        image = pygame.image.load(os.path.join('res', path_to_spritesheet))

        if scaled_dimensions == (0, 0):
            self.sprite_sheet = image
            self.s_width = self.width
            self.s_height = self.height
        else:
            self.sprite_sheet = pygame.transform.scale(image, (self.s_width * num_frames, self.s_height))

    def drawSprite(self, window, position, frame, flip_x=False):
        x, y = position
        offset = frame * self.s_width

        if flip_x:
            sprite = pygame.Surface((self.s_width, self.s_height))
            sprite.blit(self.sprite_sheet, (0, 0), (offset, 0, self.s_width, self.s_height))
            reversed_sprite = pygame.transform.flip(sprite, True, False) #Flip horizontally
            reversed_sprite.set_colorkey((0,0,0))
            window.blit(reversed_sprite, (x,y))
        else:
            window.blit(self.sprite_sheet, (x,y), (offset, 0, self.s_width, self.s_height))
