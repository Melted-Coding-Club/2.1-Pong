import pygame

pygame.init()  # Initializes pygame. This is required for pygame to function properly

# Window setup
screen = pygame.display.set_mode((800, 600))  # This will create a window in the variable screen
pygame.display.set_caption('Pong')  # This changes the name at the top of the window
clock = pygame.time.Clock()  # Creates a clock object, this allows us to control the speed our program calculates each frame
fps = 60  # This is a simple integer variable to control our frames per second (fps)

while True:  # This creates our infinite loop for us to calculate and display each from of our game
    # Event handling
    for event in pygame.event.get():  # pygame.event.get() retrieves all the events in the queue. Events that occur are added to the queue to be delt with by the next frame
        if event.type == pygame.QUIT:  # Filters the event type to clicking the red X
            pygame.quit()  # Quits the pygame display object (screen)
            quit()  # Quits the current running python file

    # Rendering
    screen.fill("black")  # Fills the whole screen with black

    # Update Screen
    pygame.display.flip()  # Updates rendered parts to the display object (screen)
    clock.tick(fps)  # This ticks out clock, basically telling our program to wait before starting to calculate the next frame. This stops the program from running as fast as possible and instead at a steady framerate
