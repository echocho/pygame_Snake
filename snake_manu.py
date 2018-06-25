import pygame
pygame.init()
import snake_button

clock = pygame.time.Clock()


class Manu:
    def text_objects(self, text, font):
        textSurface = font.render(text, True, GREY)
        return textSurface, textSurface.get_rect()

    def game_intro(self, gameTitle, titleFontSize):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            screen.fill(BLACK)
            set_textFont = pygame.font.Font('freesansbold.ttf', titleFontSize)
            textSurface, textArea = self.text_objects(gameTitle, set_textFont)
            textArea.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/4))
            screen.blit(textSurface, textArea)
            # create two buttons here
            start_button = Button('start')
            start_button.create(GREY, 100, 350, 100, 50)
            start_button.mouseHoverEffect(LIGHT_GREY, 100, 350, 100, 50)
            start_button.addText('PLAY', 100, 350, 100, 50, WHITE)
            quit_button = Button('quit')
            quit_button.create(GREY, 300, 350, 100, 50)
            quit_button.mouseHoverEffect(LIGHT_GREY, 300, 350, 100, 50)
            # quit_button.addText('QUIT', 300, 350, 100, 50, WHITE)

            pygame.display.update()
            clock.tick(15)
