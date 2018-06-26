import pygame, random, time
pygame.init()

import snake_world
import snake_food
import snake_snake
import snake_manu

World = snake_world.World()
Manu = snake_manu.Manu()
Food = snake_food.Food()
Snake = snake_snake.Snake()

# -------------------
# -------------------
# CUSTOMIZED AREA
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BORDER_THICKNESS = 20
FOOD_RANGE_1 = BORDER_THICKNESS
FOOD_RANGE_2 = SCREEN_HEIGHT - 1.5*BORDER_THICKNESS
SNAKE_RECT_LEN = 10
INITIAL_SNAKE_LEN = 200
GAME_TITLE_SIZE = 38

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

INITIAL_SNAKE_X_POS = 80
INITIAL_SNAKE_Y_POS = 80
# -------------------
# -------------------

#  set screen
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


class BorderHitChecker:

    def __init__(self):
        self.status = False

    def check(self):
        (head_x_pos, head_y_pos) = Snake.head_location()
        # print('head_x_pos, head_y_pos', head_x_pos, head_y_pos)
        # print('border thickness', BORDER_THICKNESS)
        if head_x_pos < BORDER_THICKNESS or head_x_pos > SCREEN_WIDTH - BORDER_THICKNESS or head_y_pos < BORDER_THICKNESS or head_y_pos > SCREEN_HEIGHT - BORDER_THICKNESS:
            World.game_over(screen)
            print('hit border')
            self.status = True


class CollapseChecker:

    def __init__(self):
        self.status = False

    def check(self):
        if Snake.body_list[-1] in Snake.body_list[:-1]:
            World.game_over(screen)
            print('Collapse with itself')
            print('Snake.bodyList', Snake.body_list)
            # print(Snake.body_list[-1])
            # print(Snake.body_list[:-1])
            self.status = True


Manu.game_intro(screen, 'Snake of Simplicity', GAME_TITLE_SIZE)
if Manu.status_quit:
    pygame.quit()


# main game loop
def main_game_loop():

    # carry_on = True
    carry_on = None
    score = 0

    Snake.initialize_snake(screen, WHITE, INITIAL_SNAKE_X_POS, INITIAL_SNAKE_Y_POS)
    Food.initialize_food(FOOD_RANGE_1, FOOD_RANGE_2)
    # print('Food.food_list', Food.food_list)

    if Manu.status_start:
        # print('yes!')
        carry_on = True

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        # draw border
        World.draw_border(screen, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_THICKNESS)

        World.score_cal(screen, score)

        Snake.draw_snake(screen, WHITE)

        Snake.move()

        # check if snake eats the food and then generate new food:
        food_x, food_y = Food.current_location()
        snake_x, snake_y = Snake.head_location()
        print('(food_x, food_y)', (food_x, food_y))
        print('(snake_x, snake_y)', (snake_x, snake_y))
        print('Snake.body_list', Snake.body_list)
        print('len of Snake.body_list', len(Snake.body_list))

        # if snake_x >= food_x and snake_x + SNAKE_RECT_LEN >= food_x + foodRectSize:
        if snake_x == food_x and snake_y == food_y:
            print('----------------yes food in bodylist------------------')
            Snake.extend_body(food_x, food_y)
            Food.generate_food(FOOD_RANGE_1, FOOD_RANGE_2)
            score += 1
            print('--------------------------------------score------------------')
            print(score)
            World.score_cal(screen, score) # added

        Food.draw_food(screen)

        BorderHitChecker().check()
        if BorderHitChecker().status:
            carry_on = False
        
        CollapseChecker().check()
        if CollapseChecker().status:
            carry_on = False

        pygame.display.update()
        clock.tick(60)


main_game_loop()

pygame.quit()
