import pygame, random
pygame.init()

RED = (255, 0, 0)

class Food:
    foodRectSize = 10
    def __init__(self):
        self.foodList = []
        self.color = RED  
        

    def foodList():
        return self.foodList

    def currentLocation(self):
        return self.foodList[0][0], self.foodList[0][1]

    def initialize_food(self, randomStartRange, randomEndRange, divider=10):
        self.food_x_pos, self.food_y_pos = random.randint(randomStartRange, randomEndRange), random.randint(randomStartRange, randomEndRange)
        while self.food_x_pos % divider != 0 or self.food_y_pos % divider != 0:
            self.food_x_pos = random.randint(randomStartRange, randomEndRange)
            self.food_y_pos = random.randint(randomStartRange, randomEndRange)
        self.foodList.append((self.food_x_pos, self.food_y_pos))

    def generate_food(self, randomStartRange, randomEndRange, divider=10):
        self.foodList.pop(0)
        # self.food_x_pos, self.food_y_pos = random.randint(randomStartRange, randomEndRange), random.randint(randomStartRange, randomEndRange)
        while self.food_x_pos % divider != 0 or self.food_y_pos % divider != 0:
            self.food_x_pos = random.randint(randomStartRange, randomEndRange)
            self.food_y_pos = random.randint(randomStartRange, randomEndRange)
        self.foodList.append((self.food_x_pos, self.food_y_pos))
        print(self.foodList)

    def draw_food(self, Surface):
        pygame.draw.rect(Surface, self.color, [self.foodList[0][0], self.foodList[0][1], self.foodRectSize, self.foodRectSize])
        pygame.display.update()