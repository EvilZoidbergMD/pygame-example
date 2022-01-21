import pygame
import os

width = 800
height = 640
window = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption("Pong")



#--------------------YOUR CODE GOES INSIDE HERE---------------------------


player1_x = 60
player1_y = 200

paddle_height = 100
paddle_width = 25
paddle_speed = 2

ball_x = 400
ball_y = 400
ball_dx = 2
ball_dy = 2
ball_size = 15


def update(keys_pressed):
    global player1_x
    global player1_y
    global paddle_speed
    global ball_x
    global ball_y
    global ball_dx
    global ball_dy

    if keys_pressed[pygame.K_s]:
        player1_y = player1_y + paddle_speed

    if keys_pressed[pygame.K_w]:
        player1_y = player1_y - paddle_speed

    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    if ball_x < 0 or ball_x > width:
        ball_dx = ball_dx * -1

    if ball_y < 0 or ball_y > height:
        ball_dy = ball_dy * -1


def draw():
    global player1_x
    global player1_y
    global paddle_width
    global paddle_height
    global ball_x
    global ball_y
    global ball_size

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255,255,255), (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, (255,255,255), (ball_x, ball_y, ball_size, ball_size))



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
