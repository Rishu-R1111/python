
import pygame #game ko initialize kiye h
import random #randomizer h python ka
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# CONSOLE WINDOW BANNANE K LIYE
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game ka Title
pygame.display.set_caption("-NOKIA 3310wala-saanp- by R-Enterprises")
pygame.display.update()

# Game k kuch specific variables
# for game loop
exit_game = False
game_over = False

saanp_x = 45
saanp_y = 55

# khane ka saamaan wale variables
khana_x = random.randint(25, screen_width/1.5)
khana_y = random.randint(25, screen_height/1.5)

# apna score wala variable
point = 0

# SAPOLE KI VELOCITY K LIYE
velocity_x = 0
velocity_y = 0
badhti_hui_velocity = 5

saanp_size = 20

# GAME KA FRAME CHANGING RATE
fps = 30 
# ^^---AGER TERE PASS ACHA WALA DISPLAY H to)FPS WALA TO BADHA LENA 30   se   60 fps kr liyoo

ghari = pygame.time.Clock()

# predefinded FONTS K LIYE jiska size appanne 55 set kiye h
font = pygame.font.SysFont(None,55)

# pygame KA DOCUMENTATIONS CHECK KIYOOO
def screen_pr_score(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_saanp(gameWindow, color,saanp_list, saanp_size):
    for x,y in saanp_list:
        pygame.draw.rect(gameWindow, color, [x, y, saanp_size, saanp_size])


saanp_list = []
saanp_length = 1
 


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True # game se exit krne k liye

        if event.type == pygame.KEYDOWN:#key strocks catch krne k liye

            if event.key == pygame.K_RIGHT:#rightaerokey k liye function
                velocity_x = badhti_hui_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:#LEFTaerokey k liye function
                velocity_x = -badhti_hui_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:#UPaerokey k liye function
                velocity_y = - badhti_hui_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:#DOWNaerokey k liye function
                velocity_y = badhti_hui_velocity
                velocity_x = 0

    # sapoole ki gatiwidhiyoon me badlaaw k liyee
    saanp_x = saanp_x + velocity_x
    saanp_y = saanp_y + velocity_y
    

    # is loop me saapolla apna khaa leta h n thenn re set ho jata hasattr
    if abs (saanp_x - khana_x)<25 and abs(saanp_y-khana_y)<25:
        point+=1
        print("POINT = ",point*10)

        # sab kuch over lap na hojaaye issiliye ye rewrite boleto overwrite stament avoid kiye 
        khana_x = random.randint(25, screen_width/1.5)
        khana_y = random.randint(25, screen_height/1.5)

        saanp_length +=5 

# or yaha apna loop hota h khtm 
    gameWindow.fill(black)#console bgcolor 
# score ko display kr waya h console pr
    screen_pr_score("Score: " + str(point*10),red ,5,5)
    # saapoole ka orientation#
    pygame.draw.rect(gameWindow, white, [khana_x, khana_y, saanp_size, saanp_size])

    saanp_ki_munddi = []
    saanp_ki_munddi.append(saanp_x)
    saanp_ki_munddi.append(saanp_y)

    saanp_list.append(saanp_ki_munddi)

    # pygame.draw.rect(gameWindow, red, [saanp_x, saanp_y, saanp_size, saanp_size])
    plot_saanp(gameWindow, red, saanp_list, saanp_size)


    # apne display ko refresh kiya 
    pygame.display.update()
    # finally ghari ki fps set kri hasattr
    ghari.tick(fps)


pygame.quit()
quit()