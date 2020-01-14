import pygame
import random
import config as conf

from paddle import Paddle
from coin import Coin


class Level:
    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.level = level

    def createCoin(self, num_of_coins):
        while True:
            row = random.randrange(len(self.level))
            place_for_coin = random.randrange(len(self.level[row]))

            if self.level[row][place_for_coin] == " " and num_of_coins > 0:
                self.level[row] = self.level[row][:place_for_coin] + "#" + self.level[row][place_for_coin + 1:]
                num_of_coins -= 1
            if num_of_coins == 0:
                break

    def update(self, entities, paddles, coins):
        for row in self.level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = Paddle(self.x, self.y)
                    entities.add(pf)
                    paddles.append(pf)
                if col == "#":
                    coin = Coin(self.x, self.y)
                    entities.add(coin)
                    coins.append(coin)

                self.x += conf.BLOCK_WIDTH  # блоки платформы ставятся на ширине блоков
            self.y += conf.BLOCK_HEIGHT  # то же самое и с высотой
            self.x = 0
