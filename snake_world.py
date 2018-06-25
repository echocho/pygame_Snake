import pygame, time
pygame.init()

PURPLE = (255, 0, 255)
GREY = (190, 190, 190)
# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 500
# BORDER_THICKNESS = 20

class World:
    def score_cal(self, Surface, score):
        font = pygame.font.SysFont(None, 20)
        text = font.render("Scores: "+str(score), True, PURPLE)
        Surface.blit(text, (0,0))

    def message_display(self, Surface, text):
        set_textFont = pygame.font.SysFont(None,65)
        textSurface, textArea = self.text_objects(text, set_textFont)
        textArea.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
        Surface.blit(textSurface, textArea)
    
        pygame.display.update()

        time.sleep(2)

    def gameOver(self, Surface):
        self.message_display(Surface, 'Game Over!')

    def text_objects(self, text, font):
        textSurface = font.render(text, True, GREY)
        return textSurface, textSurface.get_rect()

    def draw_border(self, Surface, color, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_THICKNESS):
        pygame.draw.rect(Surface, color, [0, 0, SCREEN_WIDTH, BORDER_THICKNESS])
        pygame.draw.rect(Surface, color, [0, 0, BORDER_THICKNESS, SCREEN_HEIGHT])
        pygame.draw.rect(Surface, color, [0, SCREEN_HEIGHT - BORDER_THICKNESS, SCREEN_WIDTH, BORDER_THICKNESS])
        pygame.draw.rect(Surface, color, [SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT])
    
    # def borderHitChecker():
    #     status = False
    #     (head_x_pos, head_y_pos) = snake.headLocation() 
    #     if head_x_pos < border_thickness or head_x_pos > screen - border_thickness or head_y_pos < border_thickness or head_y_pos > screen_height - border_thickness:
    #         world.gameOver
    #         status = True
            
    # def collapseChecker():
    #     status = False
    #     if snake.bodyList[-1] in Snake.bodyList[:-1]:
    #         world.gameOver()
    #         status = True