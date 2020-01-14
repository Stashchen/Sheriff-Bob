import config as conf
from pygame import *


class Paddle(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((conf.BLOCK_WIDTH, conf.BLOCK_HEIGHT))
        self.image = image.load("images/paddle.png")
        self.rect = Rect(x, y, conf.BLOCK_WIDTH, conf.BLOCK_HEIGHT)