import pygame, random, time, copy
pygame.init()

# -------------------
# -------------------
# CUSTOMIZED AREA
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BORDER_THICKNESS = 20
FOOD_AREA_WIDE = BORDER_THICKNESS
FOOD_AREA_HEIGHT = SCREEN_HEIGHT - 1.5*BORDER_THICKNESS
SNAKE_RECT_LEN = 5
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
# -------------------
# -------------------

#  set screen
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

def gameOver():
    message_display('Game Over!')

    restart_game()
    # clear all the states

def restart_game():
    main_game_loop()

def score_cal(score):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Scores: "+str(score), True, PURPLE)
    screen.blit(text, (0,0))


def message_display(text):
    set_textFont = pygame.font.Font('freesansbold.ttf',65)
    textSurface, textArea = text_objects(text, set_textFont)
    textArea.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(textSurface, textArea)
 
    pygame.display.update()

    time.sleep(2)



def text_objects(text, font):
    textSurface = font.render(text, True, GREY)
    return textSurface, textSurface.get_rect()

def botton_text_objects(text, font, color= None):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect() 

def start_botton(active_color, inactive_color, x_pos, y_pos, width, height):
    pygame.draw.rect(screen, inactive_color, [x_pos, y_pos, width, height])
    # add mouse interaction
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
        pygame.draw.rect(screen, active_color, [x_pos, y_pos, width, height])
        if click[0] == 1:
            main_game_loop()
    set_textFont = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textArea = botton_text_objects('START', set_textFont)
    textArea.center = (x_pos+(width/2),380)
    screen.blit(textSurface, textArea)

def quit_botton(active_color, inactive_color, x_pos, y_pos, width, height):
    pygame.draw.rect(screen, inactive_color, [x_pos, y_pos, width, height])
    # add mouse interaction
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
        pygame.draw.rect(screen, active_color, [x_pos, y_pos, width, height])
        if click[0] == 1:
            pygame.quit()
            print('quit botton')
            quit()
    set_font = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textArea = botton_text_objects('QUIT', set_font)
    textArea.center = (350,380)
    screen.blit(textSurface, textArea)

def again_button(active_color, inactive_color, x_pos, y_pos, width, height):
    pygame.draw.rect(screen, inactive_color, [x_pos, y_pos, width, height])
    mouse = pygame.mouse.get_pos()
    if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
        pygame.draw.rect(screen, active_color, [x_pos, y_pos, width, height])
    set_font = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textArea = botton_text_objects('AGAIN', set_font)
    textArea.center = (350,380)
    screen.blit(textSurface, textArea)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(BLACK)
        set_textFont = pygame.font.Font('freesansbold.ttf', 40)
        textSurface, textArea = text_objects('Snake of Simplicity', set_textFont)
        textArea.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/4))
        screen.blit(textSurface, textArea)
        

        start_botton(LIGHT_GREY, GREY, 100, 350, 100, 50)
        quit_botton(LIGHT_GREY, GREY, 300, 350, 100, 50)
            
        pygame.display.update()
        clock.tick(15)
        #-----------------
        # Question and experiment:
        # Or we could change message_display() abit and use "message_display('Snake of Simplicity')" instead?
        #-----------------   


# main game loop
def main_game_loop():
    carryOn = True
    SPEED = 5
    
        # initialize a snake
    bodyList = []
    initial_tail_x_pos = 80
    initial_tail_y_pos = 80
    while initial_tail_x_pos < INITIAL_SNAKE_LEN:
        initial_tail_x_pos += SNAKE_RECT_LEN
        bodyList.append((initial_tail_x_pos, initial_tail_y_pos)) 

    # set food
    foodList = []
    food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
    food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
    foodList.append((food_x_pos, food_y_pos))

    # used to check directions
    direction_vector = (1, 0)

    score = 0
    
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        # draw border
        draw_border()
        # put into function
        pygame.draw.rect(screen, GREEN, [0, 0, SCREEN_WIDTH, BORDER_THICKNESS])
        pygame.draw.rect(screen, GREEN, [0, 0, BORDER_THICKNESS, SCREEN_WIDTH])
        pygame.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT - BORDER_THICKNESS, SCREEN_HEIGHT, BORDER_THICKNESS])
        pygame.draw.rect(screen, GREEN, [SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT])

        score_cal(score)
       
        #  keys control
        keys = pygame.key.get_pressed()

        head_x_pos = bodyList[-1][0]
        head_y_pos = bodyList[-1][1]
        
        # check direction and limit opposite direction 
        new_direction_vector = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])
        if new_direction_vector != (0, 0) and [sum(x) for x in zip(new_direction_vector, direction_vector)] != [0,0]:
            direction_vector = new_direction_vector 
        bodyList.append((head_x_pos + direction_vector[0] * SPEED, head_y_pos + direction_vector[1] * SPEED))

        # set food pool 

        # put into generate_random_food
        # divide into two functions
        while (food_x_pos, food_y_pos) in bodyList or food_x_pos % 5 != 0 or food_y_pos % 5 != 0:
            if (food_x_pos, food_y_pos) in bodyList:
                bodyList = [(food_x_pos, food_y_pos)] + bodyList
                score += 1
                score_cal(score)
                # print((food_x_pos, food_y_pos))
                # print(len(bodyList))
                # print(bodyList)
            food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
            food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
            foodList.pop(0)
            foodList.append((food_x_pos, food_y_pos))
        # if score > 2:
        #     SPEED = 10
        # draw food -- there's always only one food in foodList
        pygame.draw.rect(screen, RED, [foodList[0][0], foodList[0][1], 10, 10])
        print('draw food: ', (foodList[0][0], foodList[0][1]))
        bodyList.pop(0)
        # draw snake 
        for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
            pygame.draw.rect(screen, WHITE, [snake_rect_x_pos, snake_rect_y_pos, 10, 10])
            print('draw body: ', (snake_rect_x_pos, snake_rect_y_pos))

        # check if snake hits border
        for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
            if snake_rect_x_pos < BORDER_THICKNESS or snake_rect_x_pos > SCREEN_WIDTH-BORDER_THICKNESS or snake_rect_y_pos < BORDER_THICKNESS or snake_rect_y_pos > SCREEN_HEIGHT-BORDER_THICKNESS:
                print('hit border-game over')
                print(foodList)
                
                carryOn = False
                gameOver()

        # check if snake collaps with itself:
        if bodyList[-1] in bodyList[:-1]:
            print('hit itself-game over')
            print(bodyList)
            
            carryOn = False
            gameOver()
        
        pygame.display.update()
        clock.tick(35)
    # bodyList = snake()
    # foodList = food()
    
game_intro()
main_game_loop()


pygame.quit()


def drawBorder(screen, color, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_THICKNESS):
    pygame.draw.rect(screen, GREEN, [0, 0, SCREEN_WIDTH, BORDER_THICKNESS])
    pygame.draw.rect(screen, GREEN, [0, 0, BORDER_THICKNESS, SCREEN_WIDTH])
    pygame.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT - BORDER_THICKNESS, SCREEN_HEIGHT, BORDER_THICKNESS])
    pygame.draw.rect(screen, GREEN, [SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT])
class Snake:
    INITAL_LENGTH = 20
    def __init__():
        self.bodyList = []
    def self.extendBody(x, y)
        self.bodyList.append((x,y))
    def bodyList():
        return self.bodyList
    


class Food
   def __init__(snake):
       self.random_generate_food(snake.bodyList())

class world

class world
constants


World.WIDTH
end
Snake.INITAL_LENGTH

s = new Snake()
s.extendBody((3,4))

food_list = []
 
food_list.append(Food.new(snake, world))

class Button
def __init__(name)
self.banner = 'name'
end
def addTrigger(fun)
    fun()

start_button = Button.new('start')
start_botton.addTrigger(start)


def start:
    logic