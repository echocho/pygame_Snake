import pygame
pygame.init()

import snake_button

GREY = (190, 190, 190)
BLACK = (0, 0, 0)
LIGHT_GREY = (210, 210, 210)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

clock = pygame.time.Clock()


class Manu:

    def text_objects(self, text, font):
        text_surface = font.render(text, True, GREY)
        return text_surface, text_surface.get_rect()

    def game_intro(self, surface, game_title, title_font_size):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            surface.fill(BLACK)
            set_text_font = pygame.font.Font('freesansbold.ttf', title_font_size)
            text_surface, text_area = self.text_objects(game_title, set_text_font)
            text_area.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/4))
            surface.blit(text_surface, text_area)

            # create two buttons here
            start_button = snake_button.Button('start')
            start_button.create(surface, GREY, 100, 350, 100, 50)
            start_button.mouse_hover_effect(surface, LIGHT_GREY, 100, 350, 100, 50)
            start_button.addText(surface, 'PLAY', 100, 350, 100, 50, WHITE)

            quit_button = snake_button.Button('quit')
            quit_button.create(surface, GREY, 300, 350, 100, 50)
            quit_button.mouse_hover_effect(surface, LIGHT_GREY, 300, 350, 100, 50)
            quit_button.addText(surface, 'QUIT', 300, 350, 100, 50, WHITE)

            pygame.display.update()
            clock.tick(15)
