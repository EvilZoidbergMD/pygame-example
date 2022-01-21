import pygame
import os

class ImageLoader:
    images = {}

    def loadImage(self, path_to_image):
        if not path_to_image in self.images.keys():
            self.images[path_to_image] = pygame.image.load(os.path.join('res', path_to_image))
        return self.images[path_to_image]