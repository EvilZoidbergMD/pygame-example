from menu import *
from battle import *
import settings
import pygame

window = pygame.display.set_mode((settings.width, settings.height))
canvas = pygame.Surface((settings.width, settings.height))
fps = 60
pygame.display.set_caption("Showdown on Ganryu Island")
running = True



#--------------------YOUR CODE GOES INSIDE HERE---------------------------


#Declare any variables you need here
active_scene = 0
if settings.debug:
    active_scene = 1
scenes = [Menu(), Battle()]


#Do the game logic and update the position/physics/collision/etc
def update(keys_pressed):
    global active_scene
    global scenes
    global running

    scenes[active_scene].update(keys_pressed)

    if scenes[active_scene].done:
        if scenes[active_scene].next_scene == -1:
            running = False
        else:
            active_scene = scenes[active_scene].next_scene
            if active_scene == 1:
                scenes[1] = Battle()
            scenes[active_scene].start()


#Draw things to the screen. Notice that things drawn later are drawn on top
#of things that are drawn earlier
def draw():
    global active_scene
    global scenes
    global window
    global canvas

    scenes[active_scene].draw(canvas)
    window.blit(canvas, (0,0))



#--------------------------------------------------------------------------



def main():
    global running

    clock = pygame.time.Clock()

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
