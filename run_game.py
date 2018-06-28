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


def hit_border():
    (head_x_pos, head_y_pos) = Snake.head_location()
    if head_x_pos < BORDER_THICKNESS or head_x_pos > SCREEN_WIDTH - BORDER_THICKNESS or head_y_pos < BORDER_THICKNESS or head_y_pos > SCREEN_HEIGHT - BORDER_THICKNESS:
        print('hit border')
        return True
    return False


def collapse_itself():
    if Snake.body_list[-1] in Snake.body_list[:-1]:
        print('Collapse with itself')
        return True
    return False


def restart():
    # reset variables to default
    Snake.reset()
    Food.reset()

    Manu.game_intro(screen, 'Snake of Simplicity', GAME_TITLE_SIZE)

    if Manu.status_quit:
        pygame.quit()
    main_game_loop()


Manu.game_intro(screen, 'Snake of Simplicity', GAME_TITLE_SIZE)
if Manu.status_quit:
    pygame.quit()


def main_game_loop():

    # carry_on = True
    carry_on = None
    score = 0

    Snake.initialize_snake(screen, WHITE, INITIAL_SNAKE_X_POS, INITIAL_SNAKE_Y_POS)
    Food.initialize_food(FOOD_RANGE_1, FOOD_RANGE_2)

    if Manu.status_start:
        carry_on = True

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        World.draw_border(screen, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_THICKNESS)

        World.score_cal(screen, score)

        Snake.draw_snake(screen, WHITE)

        Snake.move()

        # check if snake eats the food and then generate new food:
        food_x, food_y = Food.current_location()
        snake_x, snake_y = Snake.head_location()

        if snake_x == food_x and snake_y == food_y:
            Snake.extend_body(food_x, food_y)
            Food.generate_food(FOOD_RANGE_1, FOOD_RANGE_2)
            score += 1

            World.score_cal(screen, score)

        Food.draw_food(screen)

        if hit_border() or collapse_itself():
            World.game_over(screen)

            restart()

        pygame.display.update()
        clock.tick(60)


main_game_loop()

pygame.quit()

