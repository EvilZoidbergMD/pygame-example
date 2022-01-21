from scene import *
import pygame
import os

class Menu(Scene):
    selected_color = (100, 100, 200)
    non_selected_color = (100, 100, 100)

    start_button = (300, 300, 200, 50)
    exit_button = (300, 400, 200, 50)

    selected = 0
    selector_cooldown = 10
    cooldown_counter = 0
    cooldown_running = False

    def __init__(self):
        pygame.font.init()
        self.menu_font = pygame.font.SysFont("arial", 20)
        self.start_text = self.menu_font.render("Start Game", True, (255, 255, 255))
        self.exit_text = self.menu_font.render("Exit", True, (255, 255, 255))

        self.start_text_location = (400 - (self.start_text.get_width() / 2), 325 - (self.start_text.get_height() / 2))
        self.exit_text_location = (400 - (self.exit_text.get_width() / 2), 425 - (self.exit_text.get_height() / 2))

    def update(self, keys_pressed):
        if self.cooldown_running:
            self.cooldown_counter -= 1

        if self.cooldown_counter == 0:
            self.cooldown_running = False

        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_w]) and self.cooldown_counter == 0:
            self.selected += 1
            self.cooldown_running = True
            self.cooldown_counter = self.selector_cooldown

            if self.selected > 1:
                self.selected = 0

        if keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]:
            if self.selected == 0:
                self.done = True
                self.next_scene = 1
            else:
                self.done = True
                self.next_scene = -1

    def draw(self, window):
        #Background
        window.fill((0, 0, 0))

        if self.selected == 0:
            pygame.draw.rect(window, self.selected_color, self.start_button)
            pygame.draw.rect(window, self.non_selected_color, self.exit_button)
        else:
            pygame.draw.rect(window, self.non_selected_color, self.start_button)
            pygame.draw.rect(window, self.selected_color, self.exit_button)

        window.blit(self.start_text, self.start_text_location)
        window.blit(self.exit_text, self.exit_text_location)
