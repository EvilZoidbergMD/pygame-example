from scene import *
from player import *
import settings
import pygame

class Battle(Scene):

    def __init__(self):
        self.player1 = Player((150, 300))
        self.player2 = Player((475, 300), True)
        self.image = pygame.image.load(os.path.join('res', 'player.png'))
        
        pygame.font.init()

        self.countdown_font = pygame.font.SysFont("arial", 20)
        self.three = self.countdown_font.render("3", True, (255, 255, 255))
        self.two = self.countdown_font.render("2", True, (255, 255, 255))
        self.one = self.countdown_font.render("1", True, (255, 255, 255))
        self.fight = self.countdown_font.render("Fight!", True, (255, 255, 255))
        self.its_a_draw = self.countdown_font.render("Draw!", True, (255, 255, 255))
        self.player1_wins = self.countdown_font.render("Player 1 Wins!", True, (255, 255, 255))
        self.player2_wins = self.countdown_font.render("Player 2 Wins!", True, (255, 255, 255))

        self.winner = None
        self.counter = 300
        self.screen_flash_max = 5
        self.screen_flash_counter = self.screen_flash_max
        self.screen_flash = False

    def screenFlash(self):
        self.screen_flash = True
        self.screen_flash_counter = self.screen_flash_max

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_ESCAPE]:
            self.done = True
            self.next_scene = 0

        if self.counter > 0:
            self.counter -= 1
        elif self.player1.alive and self.player2.alive:
            self.player1.update(keys_pressed)
            self.player2.update(keys_pressed)

            if self.player1.active_hitbox != None:
                if self.player1.active_hitbox.active:
                    x, y, width, height = self.player1.active_hitbox.position
                    hitbox = pygame.Rect(x, y, width, height)
                    x, y, width, height = self.player2.hurtbox
                    hurtbox = pygame.Rect(x, y, width, height)

                    if hitbox.colliderect(hurtbox):
                        if self.player2.parrying:
                            self.player1.frozen = True
                            self.player1.active_hitbox = None
                            self.screenFlash()
                        else:
                            self.player2.doDeath()

            if self.player2.active_hitbox != None:
                if self.player2.active_hitbox.active:
                    x, y, width, height = self.player2.active_hitbox.position
                    hitbox = pygame.Rect(x, y, width, height)
                    x, y, width, height = self.player1.hurtbox
                    hurtbox = pygame.Rect(x, y, width, height)

                    if hitbox.colliderect(hurtbox):
                        if self.player1.parrying:
                            self.player2.frozen = True
                            self.player2.active_hitbox = None
                            self.screenFlash()
                        else:
                            self.player1.doDeath()

        elif self.player1.alive:
            self.winner = self.player1_wins
            self.player1.update(keys_pressed)
            self.player2.update(keys_pressed)
        elif self.player2.alive:
            self.winner = self.player2_wins
            self.player1.update(keys_pressed)
            self.player2.update(keys_pressed)
        else:
            self.winner = self.its_a_draw
            self.player1.update(keys_pressed)
            self.player2.update(keys_pressed)

        if self.screen_flash:
            self.screen_flash_counter -= 1

            if self.screen_flash_counter == 0:
                self.screen_flash = False
                self.screen_flash_counter = self.screen_flash_max

    def draw(self, window):
        window.fill((15, 15, 15))
        pygame.draw.rect(window, (30,30,30), (0,400,settings.width,settings.height-400))

        self.player1.draw(window)
        self.player2.draw(window)

        if self.winner != None:
            window.blit(self.winner, ((settings.width / 2) - (self.winner.get_width() / 2), (settings.height / 2) - (self.winner.get_height() / 2)))

        if self.counter > 180:
            window.blit(self.three, ((settings.width / 2) - (self.three.get_width() / 2), (settings.height / 2) - (self.three.get_height() / 2)))
        elif self.counter > 120:
            window.blit(self.two, ((settings.width / 2) - (self.two.get_width() / 2), (settings.height / 2) - (self.two.get_height() / 2)))
        elif self.counter > 60:
            window.blit(self.one, ((settings.width / 2) - (self.one.get_width() / 2), (settings.height / 2) - (self.one.get_height() / 2)))
        elif self.counter > 0:
            window.blit(self.fight, ((settings.width / 2) - (self.fight.get_width() / 2), (settings.height / 2) - (self.fight.get_height() / 2)))

        if self.screen_flash:
            window.fill((255, 255, 255, 50))
