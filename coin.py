import config as conf
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((conf.BLOCK_WIDTH, conf.BLOCK_HEIGHT))
        self.image = pygame.image.load("images/coin.png")
        self.rect = pygame.Rect(x, y, conf.BLOCK_WIDTH, conf.BLOCK_HEIGHT)