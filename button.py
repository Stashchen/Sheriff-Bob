import pygame
import config as conf

class Button:
    def __init__(self, width, height, not_active_color=(255, 0, 0), active_color=(0, 255, 0)):
        self.width = width
        self.height = height
        self.height = height
        self.not_active_color = not_active_color
        self.active_color = active_color

    def draw(self, display, x, y, message, move_x, action=None, font_size=72):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(display, self.not_active_color, (x, y, self.width, self.height))

        conf.printText(display=display, message=message, x=x + move_x, y=y + 10, font_size=font_size)






