import pygame
pygame.init()

clock = pygame.time.Clock()
SNAKE_RECT_LEN = 10
INITIAL_SNAKE_LEN = 200
SPEED = 5
direction_vector = (1, 0)

class Snake:

    def __init__(self):
        self.bodyList = []

    def extendBody(self, x, y):
        self.bodyList = [(x,y)] + self.bodyList
        self.bodyList.pop(0)

    def bodyList():
        return self.bodyList

    def headLocation(self):
        return self.bodyList[-1][0], self.bodyList[-1][1]

    def initialize_snake(self, Surface, color, ini_x_pos, ini_y_pos):
        while ini_x_pos + SNAKE_RECT_LEN <= INITIAL_SNAKE_LEN:
            self.bodyList.append((ini_x_pos, ini_y_pos))
            ini_x_pos += SNAKE_RECT_LEN
        # pygame.display.update()
        # clock.tick(35)

    def draw_snake(self, Surface, color):
        for (x, y) in self.bodyList:
            pygame.draw.rect(Surface, color, [x, y, SNAKE_RECT_LEN, SNAKE_RECT_LEN])
        
        pygame.display.update()
        clock.tick(35)

    def move(self):
        global direction_vector
        keys = pygame.key.get_pressed()
        head_x_pos, head_y_pos = self.headLocation()
        new_direction_vector = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])
        if new_direction_vector != (0, 0) and [sum(x) for x in zip(new_direction_vector, direction_vector)] != [0,0]:
            direction_vector = new_direction_vector 
        self.bodyList.append((head_x_pos + direction_vector[0] * SPEED, head_y_pos + direction_vector[1] * SPEED))
        self.bodyList.pop(0)