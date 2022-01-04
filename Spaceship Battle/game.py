import pygame
import os
import random

width = 800
height = 640
window = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption("Spaceship Battle")



#--------------------YOUR CODE GOES INSIDE HERE---------------------------



#Declare any variables you need here
player = pygame.Rect(380, 500, 32, 32)
player_speed = 3
player_alive = True
player_bullet = pygame.Rect(0, 0, 4, 10)
player_bullet_speed = 8
player_bullet_active = False

enemy = pygame.Rect(380, 100, 64, 64)
enemy_speed = 2
enemy_destination = 380 #Where the enemy ship is trying to get to
enemy_alive = True
enemy_bullet = pygame.Rect(0, 0, 4, 10)
enemy_bullet_speed = 8
enemy_bullet_active = False

game_running = True


#Import sprites here
player_image = pygame.transform.scale(pygame.image.load(os.path.join('res', 'ship.png')), (32, 32))
enemy_image = pygame.transform.scale(pygame.image.load(os.path.join('res', 'enemy.png')), (64, 64))
background_image = pygame.transform.scale(pygame.image.load(os.path.join('res', 'background.png')), (800, 816))
player_bullet_image = pygame.image.load(os.path.join('res', 'player_bullet.png'))
enemy_bullet_image = pygame.image.load(os.path.join('res', 'enemy_bullet.png'))
you_win_image = pygame.image.load(os.path.join('res', 'you win.png'))
game_over_image = pygame.image.load(os.path.join('res', 'game over.png'))


#Do the game logic and update the position/physics/collision/etc
def update(keys_pressed):
    if game_running:
        player_movement(keys_pressed)
        enemy_movement()
        player_bullet_movement()
        enemy_bullet_movement()
        check_bullet_collision()


def player_movement(keys_pressed):
    global player
    global player_speed
    global player_bullet_active

    #If the A key is pressed, move the player to the left
    if keys_pressed[pygame.K_a]:
        #Check to make sure the player doesn't go off the left of the screen
        if player.x > 0:
            player.x = player.x - player_speed
    #If the D key is pressed, move the player to the right
    if keys_pressed[pygame.K_d]:
        #Check to make sure the player doesn't go off the right of the screen
        if player.x < 800 - player.width:
            player.x = player.x + player_speed

    #If there is no active bullet, and the shoot key is pressed, shoot
    if keys_pressed[pygame.K_SPACE] and not player_bullet_active:
        player_shoot()


def enemy_movement():
    global enemy
    global enemy_speed
    global enemy_destination

    #If the ship is at it's destination: shoot then pick a new destination
    if enemy.x == enemy_destination:
        #Don't shoot if there is already an active bullet
        if not enemy_bullet_active:
            enemy_shoot()
        enemy_destination = random_destination()
    #If the destination is to the left move left
    elif enemy.x > enemy_destination:
        enemy.x -= enemy_speed
    #If the destination is to teh right move right
    elif enemy.x < enemy_destination:
        enemy.x += enemy_speed


def enemy_shoot():
    global enemy
    global enemy_bullet
    global enemy_bullet_active

    #Set the bullet's position to the bottom middle of the ship
    enemy_bullet.x = enemy.centerx - enemy_bullet.width / 2
    enemy_bullet.y = enemy.bottom
    enemy_bullet_active = True


def player_shoot():
    global player
    global player_bullet
    global player_bullet_active

    #Set the bullet's position to the top middle of the ship
    player_bullet.x = player.centerx - player_bullet.width / 2
    player_bullet.y = player.top
    player_bullet_active = True


def player_bullet_movement():
    global player_bullet
    global player_bullet_active
    global player_bullet_speed

    if player_bullet_active:
        #Player bullet always goes up
        player_bullet.y -= player_bullet_speed

    #If the bullet is off the screen, deactivate it
    if player_bullet.y < -10:
        player_bullet_active = False


def enemy_bullet_movement():
    global enemy_bullet
    global enemy_bullet_active
    global enemy_bullet_speed

    if enemy_bullet_active:
        #Enemy bullet always goes down
        enemy_bullet.y += enemy_bullet_speed

    #If the bullet is off the screen, deactivate it
    if enemy_bullet.y > 650:
        enemy_bullet_active = False


def enemy_ship_shot():
    global game_running
    global win

    win = True
    game_running = False


def player_ship_shot():
    global game_running
    global win

    win = False
    game_running = False


#Check if either bullet has collided with the ships
def check_bullet_collision():
    global player
    global enemy
    global player_bullet
    global enemy_bullet

    #Check player bullet vs enemy ship
    if player_bullet.colliderect(enemy):
        enemy_ship_shot()

    #Check enemy bullet vs player ship
    if enemy_bullet.colliderect(player):
        player_ship_shot()


#Returns a random number between 0 and 736
def random_destination():
    global enemy_speed
    return random.randrange(0, 764, enemy_speed)


#Draw things to the screen. Notice that things drawn later are drawn on top
#of things that are drawn earlier
def draw():
    global width
    global height
    global player
    global player_image
    global player_bullet
    global player_bullet_image
    global player_bullet_active
    global enemy
    global enemy_image
    global enemy_bullet
    global enemy_bullet_image
    global enemy_bullet_active
    global background_image
    global game_running
    global win
    global you_win_image
    global game_over_image

    #Draw the background
    window.blit(background_image, (0, 0))

    #Draw the player image
    window.blit(player_image, (player.x, player.y))

    #Draw the enemy image
    window.blit(enemy_image, (enemy.x, enemy.y))

    #If the bullets are active, draw them.
    if enemy_bullet_active:
        window.blit(enemy_bullet_image, (enemy_bullet.x, enemy_bullet.y))
    if player_bullet_active:
        window.blit(player_bullet_image, (player_bullet.x, player_bullet.y))

    #If the game is over, display the win or lose message
    if not game_running:
        #If the player won, show the win message (centered)
        if win:
            window.blit(you_win_image, (width / 2 - you_win_image.get_width() / 2, height / 2 - you_win_image.get_height() / 2))
        #If the player lost, show the game over message (centered)
        else:
            window.blit(game_over_image, (width / 2 - game_over_image.get_width() / 2, height / 2 - game_over_image.get_height() / 2))



#--------------------------------------------------------------------------



def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        #Limit the game to 60 frames per second
        clock.tick(fps)

        #Check the events in pygame
        for event in pygame.event.get():
            #If the user exited the window
            if event.type == pygame.QUIT:
                #Stop the loop
                running = False

        keys_pressed = pygame.key.get_pressed()

        #Main game logic
        update(keys_pressed)
        draw()

        #Update the display
        pygame.display.update()

    #If the loop has ended it is time to quit the game
    pygame.quit()


#Magic words that make python work
if __name__ == "__main__":
    main()
