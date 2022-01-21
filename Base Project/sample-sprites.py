import pygame
from util.simplegame import *
from util.sprite import *
from util.spritesheet import *
from util.animation import *
from util.animatedsprite import *


class MyGame(SimpleGame):

    def __init__(self, title='MyGame'):
        super().__init__(title)

        self.sprite = Sprite('player.png', 100, 100)

        self.spritesheet = SpriteSheet('Biker_run.png', 48, 48)
        self.animatedsprite = AnimatedSprite(100, 200, 48, 48)
        self.animatedsprite.addAnimation(Animation(self.spritesheet, 0, 5, [6,6,6,6,6,6], True))

    def update(self, keys_pressed):
        self.sprite.update(keys_pressed)
        self.animatedsprite.update(keys_pressed)

    def draw(self, window):
        window.fill((0,0,0))

        self.sprite.draw(window)
        self.animatedsprite.draw(window)


if __name__ == "__main__":
    game = MyGame('Sprites and Animations')
    game.start()
