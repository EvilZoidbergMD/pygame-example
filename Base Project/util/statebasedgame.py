import pygame

class StateBasedGame:

    def __init__(self, title='Game'):
        self.width = 800
        self.height = 640
        self.window = pygame.display.set_mode((self.width, self.height))
        self.fps = 60
        self.running = False
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(title)

        self.states = []
        self.activestate = 0

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

            self.keys_pressed = pygame.key.get_pressed()

            self.states[self.activestate].update(self.keys_pressed)
            self.states[self.activestate].draw(self.window)

            pygame.display.update()

            if self.states[self.activestate].running == False:
                self.activestate = self.states[self.activestate].next_state

                if self.activestate == -1:
                    self.running = False
                else:
                    self.states[self.activestate].start()

        #If the loop has ended it is time to quit the game
        pygame.quit()

    def addState(self, state):
        self.states.append(state)

    def removeState(self, state):
        self.states.remove(state)