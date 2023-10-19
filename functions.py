import pygame
from pygame.locals import *
import variables as vars
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.position, 10)

    def move_left(self):
        self.velocity = (-1, self.velocity[1])

    def move_right(self):
        self.velocity = (1, self.velocity[1])


def blit_text(txt: str, x: int, y: int, size: int=30, colour: tuple=(0, 0, 0), outline: bool=False, centerx: bool=False) -> None:
    font = pygame.font.SysFont(None, size)
    txt = txt.split("\n")
    for i in range(len(txt)):
        main_text = font.render(txt[i], True, colour)
        if centerx:
            x = 650 - main_text.get_width() // 2
        if outline:
            outline_text = font.render(txt[i], True, (0, 0, 0))
            vars.screen.blit(outline_text, (x, y + 1 + i * 30))
            vars.screen.blit(outline_text, (x, y - 1 + i * 30))
            vars.screen.blit(outline_text, (x - 1, y + i * 30))
            vars.screen.blit(outline_text, (x + 1, y + i * 30))
            vars.screen.blit(outline_text, (x + 1, y + 1 + i * 30))
            vars.screen.blit(outline_text, (x + 1, y - 1 + i * 30))
            vars.screen.blit(outline_text, (x - 1, y + 1 + i * 30))
            vars.screen.blit(outline_text, (x - 1, y - 1 + i * 30))
        vars.screen.blit(main_text, (x, y + i * 30))


def story(text: str, options: list=[]):
    if text[-2] != "?":
        vars.screen.fill((255, 255, 255))
        blit_text(text, 100, 600, centerx=True, colour=(0, 0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return
    else:
        user_input = ""
        options_string = options[0]
        for option in options[1:]:
            options_string += ", "
            options_string += option
        while True:
            for event in pygame.event.get():
                vars.screen.fill((255, 255, 255))
                blit_text(text, 100, 600, centerx=True, colour=(0, 0, 0))
                blit_text(user_input, 645 - 9 * len(user_input), 528, 40, colour=(0, 0, 0), outline=True)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(user_input) > 0:
                            user_input = user_input[: -1]
                    elif event.key in range(97, 123) or event.key in range(48, 58) or event.key == pygame.K_SPACE:
                        if len(user_input) < 20:
                            user_input += chr(event.key).upper()
                            pygame.draw.rect(vars.screen, (0, 0, 0), Rect(449, 509, 402, 62), 4)
                    elif event.key == pygame.K_RETURN:
                        if user_input in options:
                            return user_input
                        else:
                            story("Enter one of" + options_string)
                pygame.display.flip()
