# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import config as conf
import pygame
from coin import Coin
from pygame import *


class Player(sprite.Sprite):
    def __init__(self, x, y, image_path):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.rect = Rect(x, y, conf.WIDTH, conf.HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле?
        self.is_left = False
        self.is_right = False
        self.score = 0

        self.player_idle = pygame.image.load("{}/Idle.png".format(image_path))

        self.player_right = [pygame.image.load("{}/Right1.png".format(image_path)),
                             pygame.image.load("{}/Right2.png".format(image_path)),
                             pygame.image.load("{}/Right1.png".format(image_path)),
                             pygame.image.load("{}/Right3.png".format(image_path))]

        self.player_left = [pygame.image.load("{}/Left1.png".format(image_path)),
                            pygame.image.load("{}/Left2.png".format(image_path)),
                            pygame.image.load("{}/Left1.png".format(image_path)),
                            pygame.image.load("{}/Left3.png".format(image_path))]

        self.player_jump_idle = pygame.image.load("{}/IdleJump.png".format(image_path))
        self.player_jump_right = pygame.image.load("{}/JumpRight.png".format(image_path))
        self.player_jump_left = pygame.image.load("{}/JumpLeft.png".format(image_path))

        self.image = self.player_idle

    def update(self, left, right, up, platforms, coins):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -conf.JUMP_POWER

        if left:
            self.xvel = -conf.MOVE_SPEED  # Лево = x- n
            self.is_left = True
            self.is_right = False
            for img in self.player_left:
                self.image = img

        if right:
            self.xvel = conf.MOVE_SPEED  # Право = x + n
            self.is_left = False
            self.is_right = True
            for img in self.player_right:
                self.image = img

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.is_left = False
            self.is_right = False
            self.image = self.player_idle

        if not self.onGround:
            self.yvel += conf.GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def catch(self, to_catch, screen, game_time, entities):
        if game_time > 60 or len(entities) == 290:
            conf.showGameResult(screen, "Robber wins")

        if sprite.collide_rect(self, to_catch):
            if (self.rect.right > to_catch.rect.left and self.rect.right < to_catch.rect.right) or \
                    (self.rect.left < to_catch.rect.right and self.rect.left > to_catch.rect.left) or \
                    (self.rect.bottom > to_catch.rect.top and self.rect.bottom < to_catch.rect.bottom) or \
                    (self.rect.top < to_catch.rect.bottom and self.rect.top > to_catch.rect.top):
                conf.showGameResult(screen, "Bob wins!!!")



    def getCoin(self, coins):
        for coin in coins:
            if sprite.collide_rect(self, coin):
                coin.kill()



    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
