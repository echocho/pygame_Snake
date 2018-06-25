import pygame, random
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)

class Button:
    def __init__(self, name):
        self.banner = name
    
    def text_objects(self, text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect() 

    def create(self, Surface, inactive_color, x_pos, y_pos, width, height):
        pygame.draw.rect(Surface, inactive_color, [x_pos, y_pos, width, height])

    def mouseHoverEffect(self, Surface, active_color, x_pos, y_pos, width, height):
        mouse = pygame.mouse.get_pos()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            pygame.draw.rect(Surface, active_color, [x_pos, y_pos, width, height])
        
    def addText(self, Surface, text, x_pos, y_pos, width, height, color):
        set_textFont = pygame.font.SysFont('arial.ttf', 25)
        textSurface, textArea = self.text_objects('start', set_textFont)
        textArea.center = (x_pos+(width/2), (y_pos + height/2))
        Surface.blit(textSurface, textArea)
        pygame.display.update()
    
    def addTrigger(self, x_pos, y_pos, width, height):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            if click[0] == 1:
                if self.banner == 'start':
                    print('click start')
                if self.banner == 'quit':
                    print('click quit')
