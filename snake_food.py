import pygame, random
pygame.init()

RED = (255, 0, 0)


class Food:

    foodRectSize = 10

    def __init__(self):
        self.food_list = []
        self.color = RED
        self.food_x_pos = None
        self.food_y_pos = None

    def food_list(self):
        return self.food_list

    def current_location(self):
        return self.food_list[0][0], self.food_list[0][1]

    def initialize_food(self, random_start_range, random_end_range, divider=10):
        self.food_x_pos, self.food_y_pos = random.randint(random_start_range, random_end_range), random.randint(random_start_range, random_end_range)

        while self.food_x_pos % divider != 0 or self.food_y_pos % divider != 0:
            self.food_x_pos = random.randint(random_start_range, random_end_range)
            self.food_y_pos = random.randint(random_start_range, random_end_range)
        self.food_list.append((self.food_x_pos, self.food_y_pos))

        return self.food_list

    def generate_food(self, random_start_range, random_end_range, divider=10):
        self.food_list.pop(0)

        # self.food_x_pos, self.food_y_pos = random.randint(random_start_range, random_end_range), random.randint(random_start_range, random_end_range)
        while self.food_x_pos % divider != 0 or self.food_y_pos % divider != 0:
            self.food_x_pos = random.randint(random_start_range, random_end_range)
            self.food_y_pos = random.randint(random_start_range, random_end_range)
        self.food_list.append((self.food_x_pos, self.food_y_pos))
        print('self.food_list', self.food_list)

        return self.food_list

    def draw_food(self, surface):
        pygame.draw.rect(surface, self.color, [self.food_list[0][0], self.food_list[0][1], self.foodRectSize, self.foodRectSize])
        pygame.display.update()
