from util.statebasedgame import *
from util.gamestate import *


class FlashingState(GameState):

    def __init__(self, parent):
        super().__init__(parent)

        self.color = 0
        self.up = True

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_2]:
            self.running = False
            self.next_state = 1

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


class BouncingState(GameState):

    def __init__(self, parent):
        super().__init__(parent)

        self.next_state = 0
        self.ball_x = 100
        self.ball_y = 100
        self.ball_size = 25
        self.ball_dx = 2
        self.ball_dy = 2

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_1]:
            self.running = False
            self.next_state = 0

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_x < 0 or self.ball_x + self.ball_size > game.width:
            self.ball_dx *= -1
        if self.ball_y < 0 or self.ball_y + self.ball_size > game.height:
            self.ball_dy *= -1

    def draw(self, window):
        window.fill((0,0,0))

        pygame.draw.rect(window, (255,255,255), (self.ball_x, self.ball_y, self.ball_size, self.ball_size))


if __name__ == '__main__':
    game = StateBasedGame('A Game With Multiple States')
    game.addState(FlashingState(game))
    game.addState(BouncingState(game))
    game.start()
