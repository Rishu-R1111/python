

import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True # game se exit krne k liye


        if event.type == pygame.KEYDOWN: #keyboard se input liye h   


            if event.key == pygame.K_RIGHT: #rightaerokey k liye function
                print("AARE RIGHT AEROKEY PRESS KIYE HO")
            # if event.key == pygame.K_RIGHT: #rightaerokey k liye function
            #     print("AARE RIGHT AEROKEY PRESS KIYE HO")
            
            
            if event.key == pygame.K_LEFT: #_LEFTaerokey k liye function
                print("AARE _LEFT AEROKEY PRESS KIYE HO")


            if event.key == pygame.K_UP:#UPaerokey k liye function
                print("ABEE UP AEROKEY PRESS KIYE HO ")
            
            
            if event.key == pygame.K_DOWN:#DOWNaerokey k liye function
                print("ABEE DOWN AEROKEY PRESS KIYE HO ")

            


pygame.quit()
quit()
