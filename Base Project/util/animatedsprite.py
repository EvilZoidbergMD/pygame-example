from util.imageloader import *
from util.sprite import *


class AnimatedSprite(Sprite):

    def __init__(self, position, size, colorkey=(0,0,0)):
        super().__init__(None, position, size, colorkey)

        self.animations = []
        self.active_animation = 0
        self.flip = (False,False)

    def addAnimation(self, animation):
        self.animations.append(animation)

    def playAnimation(self, index):
        self.active_animation = index

    def update(self, keys_pressed):
        self.animations[self.active_animation].update()

    def draw(self, window):
        self.animations[self.active_animation].draw(window, (self.x, self.y), (self.width, self.height), self.flip)

    def flipX(self):
        self.flip = (not self.flip[0], self.flip[1])

    def flipY(self):
        self.flip = (self.flip[0], not self.flip[1])
