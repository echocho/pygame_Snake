import pygame

pygame.init()

clock = pygame.time.Clock()


class Snake:

    def __init__(self):
        self.body_list = []
        (self.pop_x, self.pop_y) = (0, 0)
        self.direction_vector = (1, 0)
        self.SNAKE_RECT_LEN = 10
        self.INITIAL_SNAKE_LEN = 300
        self.SPEED = 5

    def extend_body(self, x, y):
        self.body_list = [(self.pop_x, self.pop_y)] + self.body_list
        # print('self.body_list', self.body_list)
        # print('len of self.body_list', self.body_list)

    def body_list(self):
        return self.body_list

    def head_location(self):
        return self.body_list[-1][0], self.body_list[-1][1]

    def initialize_snake(self, surface, color, ini_x_pos, ini_y_pos):
        while ini_x_pos + self.SNAKE_RECT_LEN <= self.INITIAL_SNAKE_LEN:
            self.body_list.append((ini_x_pos, ini_y_pos))
            ini_x_pos += self.SNAKE_RECT_LEN

    def draw_snake(self, surface, color):
        for (x, y) in self.body_list:
            pygame.draw.rect(surface, color, [x, y, self.SNAKE_RECT_LEN, self.SNAKE_RECT_LEN])

    def move(self):
        keys = pygame.key.get_pressed()
        head_x_pos, head_y_pos = self.head_location()
        new_direction_vector = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

        if new_direction_vector != (0, 0) and [sum(x) for x in zip(new_direction_vector, self.direction_vector)] != [0,0]:
            self.direction_vector = new_direction_vector

        self.body_list.append((head_x_pos + self.direction_vector[0] * self.SPEED, head_y_pos + self.direction_vector[1] * self.SPEED))
        (self.pop_x, self.pop_y) = self.body_list.pop(0)

    def reset(self):
        self.body_list = []
        (self.pop_x, self.pop_y) = (0, 0)
        self.direction_vector = (1,0)
