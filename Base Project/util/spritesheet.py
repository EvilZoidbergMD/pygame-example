import pygame
from util.imageloader import *

class SpriteSheet:

    def __init__(self, path_to_image, tile_width, tile_height, colorkey=(0,0,0)):
        self.image = ImageLoader().loadImage(path_to_image)
        self.colorkey = colorkey

        self.tile_width = tile_width
        self.tile_height = tile_height

        self.total_width = self.image.get_width()
        self.total_height = self.image.get_height()

        self.tiles_in_row = int(self.total_width / tile_width)

    def getSubImage(self, location):
        x, y, width, height = location
        surf = pygame.Surface((width, height))
        surf.set_colorkey(self.colorkey)
        surf.blit(self.image, (0,0), location)
        return surf

    def getImageByIndex(self, index, size, flip=(False,False)):
        surf = pygame.Surface(size)
        surf.set_colorkey(self.colorkey)
        image = self.getSubImage(self.getLocationForIndex(index))
        surf.blit(pygame.transform.scale(image, size), (0,0))
        surf = pygame.transform.flip(surf, flip[0], flip[1])

        return surf

    def getScaledImageByIndex(self, index, size):
        return getImageByIndex(self, index, size)

    def getFlippedImageByIndex(self, index, flipX, flipY):
        return getImageByIndex(self, index, (self.tile_width,self.tile_height), (flipX,flipY))

    def getLocationForIndex(self, index):
        row = 0

        while index > self.tiles_in_row:
            row += 1
            index -= self.tiles_in_row

        x = index * self.tile_width
        y = row * self.tile_height

        return (x, y, self.tile_width, self.tile_height)
