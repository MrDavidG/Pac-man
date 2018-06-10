# -*- coding: utf-8 -*-
import sys
import settings as Settings
import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption("Catch Me If You CAN")

    wall = pygame.image.load("./figures/wall.png").convert_alpha()
    path = pygame.image.load("./figures/path.png").convert_alpha()
    wall = pygame.transform.scale(wall, (30, 30))
    path = pygame.transform.scale(path, (30, 30))

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都会重绘屏幕
        screen.fill(Settings.bg_color)

        # 绘制背景
        matrix = Settings.MAP
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if (matrix[i][j] == 1):
                    screen.blit(wall, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
                elif (matrix[i][j] == 0):
                    screen.blit(path, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))

        # 绘制对象



        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
