import pygame, random, time
pygame.init()
import snake_world
World = snake_world.World()
import snake_button
Button = snake_world.World()
import snake_manu 
Manu = snake_manu.Manu()
import snake_food 
Food = snake_food.Food()
import snake_snake
Snake = snake_snake.Snake()

# -------------------
# -------------------
# CUSTOMIZED AREA
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BORDER_THICKNESS = 20
FOOD_RANGE_1 = BORDER_THICKNESS
FOOD_RANGE_2 = BORDER_THICKNESS = SCREEN_HEIGHT - 1.5*BORDER_THICKNESS
SNAKE_RECT_LEN = 10
INITIAL_SNAKE_LEN = 200
BLACK = (0, 0, 0)
GREEN = (20, 255, 140)
LIGHT_GREY = (210, 210, 210)
GREY = (190, 190, 190)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
SPEED = 5
foodRectSize = 10
# -------------------
# -------------------

#  set screen
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

class BorderHitChecker:
    def __init__(self):
        self.status = False
    def check():
        (head_x_pos, head_y_pos) = Snake.headLocation() 
        if head_x_pos < BORDER_THICKNESS or head_x_pos > SCREEN_WIDTH - BORDER_THICKNESS or head_y_pos < BORDER_THICKNESS or head_y_pos > SCREEN_HEIGHT - BORDER_THICKNESS:
            World.gameOver(screen)
            print('hit border')
            self.status = True
        
class CollapseChecker:
    def __init__(self):
        self.status = False
    def check():
        if Snake.bodyList[-1] in Snake.bodyList[:-1]:
            World.gameOver(screen)
            print('collapes with itself')
            print(Snake.bodyList)
            self.status = True

# main game loop
def main_game_loop():
    carryOn = True
    score = 0
   

    Snake.initialize_snake(screen, WHITE, 80, 80)
    Food.initialize_food(FOOD_RANGE_1, FOOD_RANGE_2)
    print(Food.foodList)

    

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        # World.draw_border(screen, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_THICKNESS)
        World.draw_border(screen, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, 20)

        Snake.move()
        
       
        # check if snake eats the food and then generate new food:
        food_x, food_y = Food.currentLocation()
        snake_x, snake_y = Snake.headLocation()
        # print((food_x, food_y))

        if snake_x >= food_x and snake_x + SNAKE_RECT_LEN >= food_x + foodRectSize:
            print('yes food in bodylist')
            Snake.extendBody(food_x, food_y)
            Food.generate_food(FOOD_RANGE_1, FOOD_RANGE_2)

        Food.draw_food(screen)

        

        World.score_cal(screen, score)
        

        Snake.draw_snake(screen, WHITE)


        # check if snake hits border
        # BorderHitChecker.check()
        # if BorderHitChecker().status == True:
        #     carryOn = False
        
        # CollapseChecker.check()
        # if CollapseChecker().status == True:
        #     carryOn = False
        
            
        # pygame.display.update()
        # clock.tick(35)

main_game_loop()

pygame.quit()

    
