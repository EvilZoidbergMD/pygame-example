

class Animation:
    
    def __init__(self, sprite_sheet, begin, end, frame_times, repeat=False):
        self.is_playing = False
        self.current_frame = 0
        self.current_frame_counter = 0
        self.sprite_sheet = sprite_sheet
        self.begin = begin
        self.end = end
        self.frame_times = frame_times
        self.repeat = repeat

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.current_frame = 0

    def stop(self):
        self.is_playing = False

    def restart(self):
        self.is_playing = True
        self.current_frame = 0

    def set_repeat(self, repeat):
        self.repeat = repeat

    def update(self):
        self.current_frame_counter += 1

        if self.current_frame_counter > self.frame_times[self.current_frame]:
            if self.current_frame < len(self.frame_times) - 1:
                self.current_frame += 1
                self.current_frame_counter = 0
            else:
                if self.repeat:
                    self.current_frame = 0
                else:
                    self.is_playing = False

    def draw(self, window, position):
        window.blit(self.sprite_sheet.getImageByIndex(self.begin + self.current_frame), position)
