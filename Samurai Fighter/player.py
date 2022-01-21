from spritesheet import *
from animation import *
from hitbox import *
import settings
import pygame

class Player:

    def __init__(self, position, facing_left=False):
        self.x, self.y = position
        self.scale = 7
        self.width = 24 * self.scale
        self.height = 24 * self.scale

        self.alive = True
        self.animations = []
        self.current_animation = 1
        self.speed = 1
        self.stance = 1 #Start in mid-stance
        self.stance_cooldown_max = 30
        self.stance_cooldown = 0
        self.attacking = False
        self.moving = False
        self.lunge_distance = 30
        self.lunged = 0
        self.lunge_speed = 10
        self.active_hitbox = None
        self.frozen = False
        self.frozen_counter_max = 45
        self.frozen_counter = self.frozen_counter_max
        self.parrying = False
        self.parry_counter_max = 10
        self.parry_counter = self.parry_counter_max
        self.facing_left = facing_left

        self.right = pygame.K_d
        self.left = pygame.K_a
        self.stance_up = pygame.K_w
        self.stance_down = pygame.K_s
        self.attack = pygame.K_SPACE

        self.sprite_sheet = SpriteSheet('player.png', 35, (24,24), (self.width,self.height))

        self.animations.append(Animation(self.sprite_sheet, 11, 11, [1], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 0, 0, [1], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 19, 19, [1], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 12, 16, [2, 2, 1, 1, 20], self.facing_left))
        self.animations.append(Animation(self.sprite_sheet, 3, 8, [2, 2, 2, 3, 3, 20], self.facing_left))
        self.animations.append(Animation(self.sprite_sheet, 20, 26, [3, 3, 3, 3, 3, 3, 20], self.facing_left))
        self.animations.append(Animation(self.sprite_sheet, 9, 10, [10, 10], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 1, 2, [10, 10], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 17, 18, [10, 10], self.facing_left, True))
        self.animations.append(Animation(self.sprite_sheet, 27, 34, [5, 5, 5, 5, 5, 5, 5, 1], self.facing_left))
        self.animations.append(Animation(self.sprite_sheet, 27, 27, [1], self.facing_left, True))

        self.low_idle = 0 #Stances are the index of the stance value
        self.mid_idle = 1
        self.high_idle = 2
        self.low_attack = 3 #Attacks are the stance value +3
        self.mid_attack = 4
        self.high_attack = 5
        self.low_walk = 6 #Walks are the stance value +6
        self.mid_walk = 7
        self.high_walk = 8
        self.death = 9
        self.froze = 10

        self.hurtbox_offsets = (8 * self.scale, 10 * self.scale)
        self.hurtbox_dimensions = (7 * self.scale, 10 * self.scale)

        #Different keys for second player
        if self.facing_left:
            self.right = pygame.K_RIGHT
            self.left = pygame.K_LEFT
            self.stance_up = pygame.K_UP
            self.stance_down = pygame.K_DOWN
            self.attack = pygame.K_RETURN

            self.lunge_speed *= -1 #lunge to the left
            self.lunge_distance *= -1
            self.hurtbox_offsets = (9 * self.scale, 10 * self.scale)

        self.updateBoxes()

    def update(self, keys_pressed):
        if self.alive:
            if not self.frozen:
                self.moving = False
                if keys_pressed[self.right] and not self.attacking:
                    self.x += self.speed
                    self.move()
                if keys_pressed[self.left] and not self.attacking:
                    self.x -= self.speed
                    self.move()
                if keys_pressed[self.stance_up] and self.stance_cooldown == 0 and self.stance < 2 and not self.attacking:
                    self.stanceUp()
                if keys_pressed[self.stance_down] and self.stance_cooldown == 0 and self.stance > 0 and not self.attacking:
                    self.stanceDown()
                if keys_pressed[self.attack] and not self.attacking:
                    self.doAttack()

            #lunge during low attack
            if self.current_animation == self.low_attack and self.lunged != self.lunge_distance:
                self.x += self.lunge_speed
                self.lunged += self.lunge_speed
                self.updateBoxes()

            if self.frozen:
                self.current_animation = self.froze
                self.animations[self.current_animation].play()

                self.frozen_counter -= 1

                if self.frozen_counter < 0:
                    self.frozen_counter = self.frozen_counter_max
                    self.frozen = False
                    self.current_animation = self.stance #Making use of clever indexing
                    self.animations[self.current_animation].play()

            elif self.attacking:
                if not self.animations[self.current_animation].is_playing:
                    self.attacking = False
                    self.lunged = 0
                    self.current_animation = self.stance #Making use of clever indexing
                    self.animations[self.current_animation].play()
                    self.active_hitbox = None
            elif self.moving:
                self.current_animation = self.stance + 6 #Making use of clever indexing
                self.animations[self.current_animation].play()
            else:
                self.current_animation = self.stance
                self.animations[self.current_animation].play()

            if self.stance_cooldown > 0:
                self.stance_cooldown -= 1

        if self.parrying:
            self.parry_counter -= 1

            if self.parry_counter < 0:
                self.parry_counter = self.parry_counter_max
                self.parrying = False

        self.animations[self.current_animation].update()

        if self.active_hitbox != None:
            self.active_hitbox.update()

    def draw(self, window):
        self.animations[self.current_animation].drawAnimation(window, (self.x, self.y))
        
        if settings.debug:
            pygame.draw.rect(window, (255,0,0), self.hurtbox, 3)
            if self.active_hitbox != None:
                self.active_hitbox.draw(window)

    def updateBoxes(self):
        x_offset, y_offset = self.hurtbox_offsets
        width, height = self.hurtbox_dimensions
        self.hurtbox = (self.x + x_offset, self.y + y_offset, width, height)

    def move(self):
        self.updateBoxes()
        self.moving = True

    def stanceUp(self):
        self.stance += 1
        self.stance_cooldown = self.stance_cooldown_max
        self.current_animation = self.stance #Making use of clever indexing
        self.animations[self.current_animation].play()

        self.parrying = True

    def stanceDown(self):
        self.stance -= 1
        self.stance_cooldown = self.stance_cooldown_max
        self.current_animation = self.stance #Making use of clever indexing
        self.animations[self.current_animation].play()

        self.parrying = True

    def doAttack(self):
        self.attacking = True
        self.current_animation = self.stance + 3 #Making use of clever indexing
        self.animations[self.current_animation].play()

        #Set hitbox
        if self.stance == 0:
            self.active_hitbox = Hitbox(self.getLowAttackPosition(), 5, 10)
        elif self.stance == 1:
            self.active_hitbox = Hitbox(self.getMidAttackPosition(), 10, 15)
        elif self.stance == 2:
            self.active_hitbox = Hitbox(self.getMidAttackPosition(), 15, 20)

    def doDeath(self):
        self.alive = False
        self.current_animation = self.death
        self.animations[self.current_animation].play()

    def getLowAttackPosition(self):
        return (self.x + self.lunge_distance, self.y, self.width, self.height)

    def getMidAttackPosition(self):
        return (self.x + (self.scale*2), self.y, self.width - (self.scale*4), self.height)

    def getHighAttackPosition(self):
        return (self.x + (self.scale*2), self.y, self.width - (self.scale*4), self.height)
