# -*- coding: utf-8 -*-
import settings as Settings
import pygame
import Map
import time
from Ghost import Ghost
from Pacman import Pacman


def loadFigure(figure):
    fig = pygame.image.load(figure).convert_alpha()
    return pygame.transform.scale(fig, (Settings.UNIT_LENGTH, Settings.UNIT_LENGTH))


def drawBlackBlock(screen, loc):
    pygame.draw.rect(screen, Settings.BG_COLOR,
                     [loc[1] * Settings.UNIT_LENGTH,
                      loc[0] * Settings.UNIT_LENGTH,
                      Settings.UNIT_LENGTH,
                      Settings.UNIT_LENGTH])


def drawMoving(screen, figure, loc_last, loc_next):
    # 消去上一个格子
    # 如果是PACMAN的规则，即吃豆豆的话
    if loc_next != loc_last:
        if Settings.PACMAN:
            drawBlackBlock(screen, loc_last)
        elif Map.get((loc_last[0], loc_last[1])) == 0:
            path = loadFigure(Settings.FIG_PATH)
            screen.blit(path, (loc_last[1] * Settings.UNIT_LENGTH, loc_last[0] * Settings.UNIT_LENGTH))
        elif Map.get((loc_last[0], loc_last[1])) == 2:
            drawBlackBlock(screen, loc_last)

        # 画下一个格子
        screen.blit(loadFigure(figure), (loc_next[1] * Settings.UNIT_LENGTH, loc_next[0] * Settings.UNIT_LENGTH))


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption("Catch Me If You CAN")
    # 绘制屏幕
    wall = loadFigure(Settings.FIG_WALL)
    path = loadFigure(Settings.FIG_PATH)
    # 绘制底色 重绘的时候会覆盖所有的画面
    screen.fill(Settings.BG_COLOR)
    # 绘制迷宫地图
    for i in range(Settings.UNIT_HEIGHT):
        for j in range(Settings.UNIT_WIDTH):
            if (Map.get((i, j)) == 1):
                screen.blit(wall, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
            elif (Map.get((i, j)) == 0):
                screen.blit(path, (j * Settings.UNIT_LENGTH, i * Settings.UNIT_LENGTH))
    # 绘制gHost
    ghost_1 = Ghost(11, 12, 'left')
    screen.blit(ghost_1.getFigure("./figures/red_right.png"), (12 * Settings.UNIT_LENGTH, 11 * Settings.UNIT_LENGTH))
    # 绘制pac-man
    pacman_1 = Pacman(11, 1, 'right')
    screen.blit(pacman_1.getFigure("./figures/Pacman_left.png"), (1 * Settings.UNIT_LENGTH, 11 * Settings.UNIT_LENGTH))
    # 让最近绘制的屏幕可见
    pygame.display.flip()

    t = 0

    # 开始游戏主循环
    while True:
        # 每一步之间的时间间隔
        # time.sleep(Settings.UNIT_INTERVAL)
        t += 1

        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # 计算并保留当前的state
        if Settings.PACMAN:
            # 如果是吃豆豆的情况下
            # TODO
            state = {'map': Settings.MAP_state}
        else:
            # 如果是不吃豆豆的情况下
            state = {'map': Settings.MAP_state, 'ghost_locations': [ghost_1.getLoc()],
                     'pacman_location': pacman_1.getLoc()}

        # 绘制gHost
        loc_last = ghost_1.getLoc()
        figure, loc_next = ghost_1.takeAction(ghost_1.getLoc(), state, Settings.ICONMAP_GHOST)
        drawMoving(screen, figure, loc_last, loc_next)
        # 绘制pac-man
        loc_last = pacman_1.getLoc()
        figure, loc_next = pacman_1.takeAction(pacman_1.getLoc(), state, Settings.ICONMAP_PACMAN)
        drawMoving(screen, figure, loc_last, loc_next)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

        # 判定胜利条件
        if ghost_1.getLoc() == pacman_1.getLoc():
            break


run_game()
