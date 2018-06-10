# -*- coding: utf-8 -*-
import sys
import settings as Settings
import pygame

from Ghost import Ghost
from Pacman import Pacman


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption("Catch Me If You CAN")

    wall = pygame.image.load("./figures/wall.png").convert_alpha()
    path = pygame.image.load("./figures/path.png").convert_alpha()
    wall = pygame.transform.scale(wall, (30, 30))
    path = pygame.transform.scale(path, (30, 30))

    # 绘制屏幕 重绘的时候会覆盖所有的画面
    screen.fill(Settings.bg_color)
    # 绘制背景
    matrix = Settings.MAP
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (matrix[i][j] == 1):
                screen.blit(wall, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
            elif (matrix[i][j] == 0):
                screen.blit(path, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
    # 绘制gHost
    ghost_1 = Ghost(11, 0)
    screen.blit(ghost_1.getFigure("./figures/red_right.png"), (12 * 30, 11 * 30))
    # 绘制pac-man
    pacman_1 = Pacman(11, 12)
    screen.blit(pacman_1.getFigure("./figures/Pacman_left_.png"), (0, 11 * 30))

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 绘制gHost
        # 前一步消失
        loc_x, loc_y = ghost_1.getLoc()
        if matrix[loc_x][loc_y] == 1:
            screen.blit(path, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
        # TODO: 函数化
        # else:
        #     screen.blit(, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
        # 下一步出现
        # 绘制pac-man

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
