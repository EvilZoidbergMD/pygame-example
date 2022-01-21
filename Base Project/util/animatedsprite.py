from util.imageloader import *
from util.sprite import *


class AnimatedSprite(Sprite):

    def __init__(self, x, y, width, height):
        super().__init__(None, x, y, width, height)

        self.animations = []
        self.active_animation = 0

    def addAnimation(self, animation):
        self.animations.append(animation)

    def playAnimation(self, index):
        self.active_animation = index

    def update(self, keys_pressed):
        self.animations[self.active_animation].update()

    def draw(self, window):
        self.animations[self.active_animation].draw(window, (self.x, self.y, self.width, self.height))
