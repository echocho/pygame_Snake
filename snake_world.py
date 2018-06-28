import pygame, time

pygame.init()

# -------------------
# -------------------
# CUSTOMIZED AREA
GREY = (190, 190, 190)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BORDER_THICKNESS = 20
# -------------------
# -------------------


class World:

    @staticmethod
    def score_cal(surface, score):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Scores: "+str(score), True, BLACK)
        surface.blit(text, (0,0))

    def message_display(self, surface, text):
        set_text_font = pygame.font.SysFont(None,65)
        text_surface, text_area = self.text_objects(text, set_text_font)
        text_area.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
        surface.blit(text_surface, text_area)
    
        pygame.display.update()

        time.sleep(2)

    def game_over(self, surface):
        self.message_display(surface, 'Game Over!')

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, GREY)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def draw_border(surface, color, screen_width, screen_height, border_thickness):
        pygame.draw.rect(surface, color, [0, 0, screen_width, border_thickness])
        pygame.draw.rect(surface, color, [0, 0, border_thickness, screen_height])
        pygame.draw.rect(surface, color, [0, screen_height - border_thickness, screen_width, border_thickness])
        pygame.draw.rect(surface, color, [screen_width - border_thickness, 0, border_thickness, screen_height])

