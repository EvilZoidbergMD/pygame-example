import pygame
import os

class SimpleGame:

    def __init__(self, title='Game'):
        self.width = 800
        self.height = 640
        self.window = pygame.display.set_mode((self.width, self.height))
        self.fps = 60
        self.running = False
        self.clock = pygame.time.Clock()
        self.mouse_down = False

        pygame.display.set_caption(title)

    def start(self):
        self.running = True

        while self.running:
            #Limit the game to 60 frames per second
            self.clock.tick(self.fps)

            #Check the events in pygame
            for event in pygame.event.get():
                #If the user exited the window
                if event.type == pygame.QUIT:
                    #Stop the loop
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseDown()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouseUp()

            self.keys_pressed = pygame.key.get_pressed()

            #Main game logic
            self.update(self.keys_pressed)
            self.draw(self.window)

            #Update the display
            pygame.display.update()

        #If the loop has ended it is time to quit the game
        pygame.quit()

    def update(self, keys_pressed):
        pass

    def draw(self, window):
        pass

    def mouseDown(self, position):
        self.mouse_down = True

    def mouseUp(self, position):
        self.mouse_down = False

    def mousePosition(self):
        return pygame.mouse.get_pos()
