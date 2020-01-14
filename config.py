import pygame
import time as t
from main import *
from button import Button
from pygame import *
from character import Player
from level import Level

pygame.init()

# ======================================================
# Main game configuration
WIN_WIDTH = 1920  # 800  # Ширина создаваемого окна
WIN_HEIGHT = 1080  # 640  # Высота
BACKGROUND_COLOR = "#ff7675"
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32

# configuration for players
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз

# ======================================================

# Sounds
pygame.mixer.music.set_volume(.1)
jump_sound = pygame.mixer.Sound("config/jump.wav")
jump_sound.set_volume(.1)

music = True

# ======================================================
# In game functions
def printText(display, message, x, y, font_type="./config/Peepo.ttf", font_color=(255, 255, 255),
              font_size=72):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def printTextWithOutline(display, message, x, y, font_type="./config/Peepo.ttf", font_color=(255, 255, 255),
                         font_size=72):
    font_type_outline = pygame.font.Font(font_type, font_size + 1)
    outline = font_type_outline.render(message, True, (0, 0, 0))
    display.blit(outline, (x, y))
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def pauseTheGame(display):
    is_paused = True
    while is_paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

        pygame.mixer.music.pause()
        printTextWithOutline(display, "Paused. Press ESC to continue.", 500, 360)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.unpause()
            is_paused = False

        pygame.display.update()


def showGameResult(screen, message):
    is_paused = True
    menu_btn = Button(650, 130, pygame.Color("#fab1a0"), pygame.Color("#fad390"))

    while is_paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == pygame.K_r:
                startGame()

        printTextWithOutline(screen, message, 800, 350)
        menu_btn.draw(screen, 650, 500, "RESTART", 200, action=startGame)
        menu_btn.draw(screen, 650, 650, "QUIT", 250, action=showMainMenu)
        pygame.display.update()


def showInstructions():
    display = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Sheriff Bob")  # Пишем в шапку
    menu_background = pygame.image.load("images/background.jpeg")
    menu_is_on = True

    global music

    while menu_is_on:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

            if e.type == KEYDOWN and e.key == pygame.K_m:
                if music:
                    pygame.mixer.music.set_volume(0)
                    music = False
                else:
                    pygame.mixer.music.set_volume(.1)
                    music = True

            if e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                showMainMenu()

            display.blit(menu_background, (0, 0))
            printText(display, "GAME RULES", 650, 20, font_size=120, font_color=pygame.Color("#eb4d4b"))
            pygame.draw.rect(display, pygame.Color("#f9ca24"), (50, 200, 1820, 780))
            printText(display, "Yellow player(Bob) need to catch green player", 100, 200,
                      font_color=(0, 0, 0))
            printText(display, "(Robber) in a minute. The Robber, in turn, need to ", 100, 300,
                      font_color=(0, 0, 0))
            printText(display, "survive this minute or collect all the coins to win.", 100, 400,
                      font_color=(0, 0, 0))

            printText(display, "Press ESC to return to the Main Menu", 300, 700,
                      font_color=(0, 0, 0))

            pygame.display.update()


def musicSettings():
    global music
    if music:
        time.delay(200)
        pygame.mixer.music.pause()
        music = False
    else:
        time.delay(200)
        pygame.mixer.music.unpause()
        music = True


def showMainMenu():
    pygame.mixer.music.load("config/Cowboy_Theme-Pavak-1711860633.wav")
    display = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Sheriff Bob")  # Пишем в шапку
    menu_background = pygame.image.load("images/background.jpeg")
    menu_is_on = True
    global music

    pygame.mixer.music.play()
    menu_btn = Button(650, 130, pygame.Color("#fab1a0"), pygame.Color("#fad390"))

    while menu_is_on:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit("QUIT")

        display.blit(menu_background, (0, 0))
        printText(display, "SHERIFF BOB", 650, 150, font_size=120, font_color=pygame.Color("#eb4d4b"))
        menu_btn.draw(display, 650, 350, "PLAY", 250, action=startGame)
        menu_btn.draw(display, 650, 500, "GAME RULES", 150, action=showInstructions)
        if music == True:
            menu_btn.draw(display, 650, 650, "MUSIC: ON", 175, action=musicSettings)
        else:
            menu_btn.draw(display, 650, 650, "MUSIC: OFF", 175, action=musicSettings)

        menu_btn.draw(display, 650, 800, "QUIT", 250, action=exit)
        pygame.display.update()


def startGame():
    global music
    pygame.init()  # Инициация PyGame, обязательная строчка
    pygame.mixer.music.load("config/battlesong.mp3")
    pygame.mixer.music.set_volume(.1)
    if music:
        pygame.mixer.music.play()


    level = [
        "------------------------------------------------------------",
        "-                                                          -",
        "-                                                          -",
        "-  ---                                                ---- -",
        "-                            -                             -",
        "-                            -                             -",
        "--                  ---      -       ----                  -",
        "-                            --                 -          -",
        "-                            -                             -",
        "-                            -                             -",
        "-          ----                                        -   -",
        "-                                                      -  --",
        "-                            -                         -   -",
        "-                            -                         -   -",
        "-                     --     -                     -----   -",
        "-       ----                 -                             -",
        "-                            -        -----                -",
        "-                                                          -",
        "-                   -                                     --",
        "-                                           -              -",
        "-                            -                 -----       -",
        "-          ---------         -                             -",
        "-                            -                           ---",
        "--                          --                             -",
        "-                            -    ---                      -",
        "-                                                          -",
        "-                                           ------         -",
        "-                   ---                                    -",
        "-   -------                  -                             -",
        "-                       ---  -       ----                  -",
        "-                            -                             -",
        "------------------------------------------------------------",
    ]

    # Стартовая настройка фона
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Sheriff Bob")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    bg.blit(pygame.image.load("images/background.jpeg"), (0, 0))

    # Начальные настройки игры
    up = up1 = False
    left = right = left1 = right1 = False  # по умолчанию — стоим
    entities = pygame.sprite.Group()  # Все объекты
    paddles = []  # то, во что мы будем врезаться или опираться
    coins = []
    num_of_coins = 10
    # Создание персонажей
    hero = Player(55, 55, "images/first_character")
    hero2 = Player(1865, 55, "images/second_character")
    level = Level(level)
    # Добавление персонажей в группу entities для последующей их прорисовки
    entities.add(hero)
    entities.add(hero2)

    # Создание таймера
    timer = pygame.time.Clock()

    # Расположение монет
    level.createCoin(num_of_coins)

    # Создание уровня
    level.update(entities, paddles, coins)

    start = t.time()
    # Основной цикл программы
    while True:

        # Настройка частоты кадров
        timer.tick(60)
        game_time = t.time() - start
        # Обрабатываем события
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")

            if e.type == KEYDOWN and e.key == K_p:
                pauseTheGame(screen)

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == KEYDOWN and e.key == K_a:
                left1 = True
            if e.type == KEYDOWN and e.key == K_d:
                right1 = True

            if e.type == KEYUP and e.key == K_d:
                right1 = False
            if e.type == KEYUP and e.key == K_a:
                left1 = False
            if e.type == KEYDOWN and e.key == K_w:
                up1 = True
            if e.type == KEYUP and e.key == K_w:
                up1 = False

        # Главная логика догонялок

        hero2.getCoin(coins)
        hero.catch(hero2, screen, game_time, entities)

        # Обновление спрайтов
        screen.blit(bg, (0, 0))
        hero.update(left1, right1, up1, paddles, coins)
        hero2.update(left, right, up, paddles, coins)
        entities.draw(screen)  # отображение
        printText(screen, "TIME: " + ("%.2f" % game_time), 870, -8, font_color=pygame.Color("#2d3436"),
                  font_size=30)
        pygame.display.update()  # обновление и вывод всех изменений на экран
