
import pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("-NOKIA 3310wala-saaps- by R-Enterprises")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
saap_x = 45
saap_y = 55
velocity_x = 0
velocity_y = 0
saap_size = 10
fps = 30

ghari = pygame.time.Clock()
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True # game se exit krne k liye

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:#rightaerokey k liye function
                velocity_x = 5
                velocity_y = 0

            if event.key == pygame.K_LEFT:#LEFTaerokey k liye function
                velocity_x = -5
                velocity_y = 0

            if event.key == pygame.K_UP:#UPaerokey k liye function
                velocity_y = - 5
                velocity_x = 0

            if event.key == pygame.K_DOWN:#DOWNaerokey k liye function
                velocity_y = 5
                velocity_x = 0

    saap_x = saap_x + velocity_x
    saap_y = saap_y + velocity_y

    gameWindow.fill(black)
    pygame.draw.rect(gameWindow, red, [saap_x, saap_y, saap_size, saap_size])
    pygame.display.update()
    ghari.tick(fps)


pygame.quit()
quit()