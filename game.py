import pygame
import os

width = 800
height = 640
window = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption("Title of the Window")



#--------------------YOUR CODE GOES INSIDE HERE---------------------------


#Declare any variables you need here
player_x = 200
player_y = 200
player_speed = 3


#Import sprites here
player_image = pygame.image.load(os.path.join('res', 'player.png'))


#Do the game logic and update the position/physics/collision/etc
def update(keys_pressed):
    global player_x
    global player_y
    global player_speed

    #If the A key is pressed, move the player to the left
    if keys_pressed[pygame.K_a]:
        player_x = player_x - player_speed
    #If the D key is pressed, move the player to the right
    if keys_pressed[pygame.K_d]:
        player_x = player_x + player_speed
    #If the W key is pressed, move the player up
    if keys_pressed[pygame.K_w]:
        player_y = player_y - player_speed
    #If the S key is pressed, move the player down
    if keys_pressed[pygame.K_s]:
        player_y = player_y + player_speed


#Draw things to the screen. Notice that things drawn later are drawn on top
#of things that are drawn earlier
def draw():
    global player_x
    global player_y

    #Fill the whole window light blue
    window.fill((100, 200, 255))

    #Draw a green rectangle at coordinates 50, 100 that is 200 pixels wide and 250 pixels tall
    pygame.draw.rect(window, (0, 150, 0), pygame.Rect(50, 100, 200, 250))

    #Draw the player image at coordinates that depend on the x and y variables
    window.blit(player_image, (player_x, player_y))



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
