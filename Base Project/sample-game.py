from util.simplegame import *


class MyGame(SimpleGame):

    def __init__(self, title='MyGame'):
        super().__init__(title)

        self.color = 0
        self.up = True

    def update(self, keys_pressed):
        if self.color == 255:
            self.up = False
        if self.color == 0:
            self.up = True

        if self.up:
            self.color += 1
        else:
            self.color -= 1

    def draw(self, window):
        window.fill((self.color,self.color,self.color))


if __name__ == "__main__":
    game = MyGame('A Simple Game')
    game.start()
