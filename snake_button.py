import pygame, random
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)

class Button:
    def __init__(self, name):
        self.banner = name
    
    def text_objects(self, text, font):
        text_surface = font.render(text, True, WHITE)
        return text_surface, text_surface.get_rect()

    def create(self, surface, inactive_color, x_pos, y_pos, width, height):
        pygame.draw.rect(surface, inactive_color, [x_pos, y_pos, width, height])

    def mouse_hover_effect(self, surface, active_color, x_pos, y_pos, width, height):
        mouse = pygame.mouse.get_pos()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            pygame.draw.rect(surface, active_color, [x_pos, y_pos, width, height])
        
    def addText(self, surface, text, x_pos, y_pos, width, height, color):
        set_text_font = pygame.font.SysFont('arial.ttf', 25)
        text_surface, text_area = self.text_objects('start', set_text_font)
        text_area.center = (x_pos+(width/2), (y_pos + height/2))
        surface.blit(text_surface, text_area)
        pygame.display.update()
    
    def add_trigger(self, x_pos, y_pos, width, height):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            if click[0] == 1:
                if self.banner == 'start':
                    print('click start')
                if self.banner == 'quit':
                    print('click quit')
