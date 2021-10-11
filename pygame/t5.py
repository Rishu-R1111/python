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
pygame.display.set_caption(" -NOKIA 3310wala-Snakes- by R-Enterprises")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False


saap_x = 45
saap_y = 55
saap_ki_size = 10
fps = 30

# ghari = pygame.time.clock()


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True # game se exit krne k liye

if event.type == pygame.KEYDOWN: #keyboard se input liye h

    if event.key == pygame.K_RIGHT:#rightaerokey k liye function
        saap_x = saap_x + 10

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [saap_x, saap_y, saap_ki_size, saap_ki_size])
    pygame.display.update()

    # ghari.tick(fps)


pygame.quit()
quit()
