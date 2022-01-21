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

    def getImageByIndex(self, index):
        return self.getSubImage(self.getLocationForIndex(index))

    def getLocationForIndex(self, index):
        row = 0

        while index > self.tiles_in_row:
            row += 1
            index -= self.tiles_in_row

        x = index * self.tile_width
        y = row * self.tile_height

        return (x, y, self.tile_width, self.tile_height)
