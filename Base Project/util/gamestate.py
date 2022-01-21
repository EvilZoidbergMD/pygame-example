

class GameState:

    def __init__(self, parent):
        self.parent = parent
        
        self.running = False
        self.next_state = 0

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def update(self, keys_pressed):
        pass

    def draw(self, window):
        pass
