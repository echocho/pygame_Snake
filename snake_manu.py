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

    def __init__(self):
        self.status_start = False
        self.status_quit = False
        self.start_x, self.start_y, self.start_w, self.start_h = 200, 450, 100, 50
        self.quit_x, self.quit_y, self.quit_w, self.quit_h = 500, 450, 100, 50

    def text_objects(self, text, font):
        text_surface = font.render(text, True, GREY)
        return text_surface, text_surface.get_rect()


    # def add_trigger(self, x_pos, y_pos, width, height):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #     if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
    #         if click[0] == 1:
    #             if self.game_intro().start_button:
    #                 print('click start')
    #                 self.status_start = True
    #             if self.game_intro().quit_button:
    #                 print('click quit')
    #                 self.status_quit = True

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
            start_button = snake_button.Button('PLAY')

            start_button.create(surface, GREY, self.start_x, self.start_y, self.start_w, self.start_h)
            start_button.mouse_hover_effect(surface, LIGHT_GREY, self.start_x, self.start_y, self.start_w, self.start_h)
            start_button.add_text(surface, self.start_x, self.start_y, self.start_w, self.start_h, WHITE)
            # self.add_trigger(start_x, start_y, start_w, start_h)

            quit_button = snake_button.Button('QUIT')

            quit_button.create(surface, GREY, self.quit_x, self.quit_y, self.quit_w, self.quit_h)
            quit_button.mouse_hover_effect(surface, LIGHT_GREY, self.quit_x, self.quit_y, self.quit_w, self.quit_h)
            quit_button.add_text(surface, self.quit_x, self.quit_y, self.quit_w, self.quit_h, WHITE)

        pygame.display.update()
        clock.tick(15)

    def trigger(self):
        print('enter trigger()')
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.start_x + self.start_w > mouse[0] > self.start_x and self.start_y + self.start_h > mouse[1] > self.start_y:
            if click[0] == 1:
                print('click start')
                self.status_start = True
            return self.status_start
        elif self.quit_x + self.quit_w > mouse[0] > self.quit_x and self.quit_y + self.quit_h > mouse[1] > self.quit_y:
            if click[0] == 1:
                self.status_quit = True
            return self.status_quit


        # pygame.display.update()
        # clock.tick(15)




