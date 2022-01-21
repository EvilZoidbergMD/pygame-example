import pygame
import settings
from animation import *

class Hitbox:

    def __init__(self, position, start, end):
        self.position = position
        self.start = start
        self.end = end

        self.counter = 0
        self.active = False

    def update(self):
        if self.counter <= self.end:
            self.counter += 1

            self.active = False
            if self.counter > self.start and self.counter < self.end:
                self.active = True

    def draw(self, window):
        if self.active and settings.debug:
            pygame.draw.rect(window, (255,0,0), self.position)
