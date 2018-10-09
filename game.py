# -*- coding: utf-8 -*-
import settings as Settings
import pygame
import Map
from Ghost import Ghost
from Pacman import Pacman
import sys
import time


def loadMusic(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()


def loadFigure(figure):
    fig = pygame.image.load(figure).convert_alpha()
    return pygame.transform.scale(fig, (Settings.UNIT_LENGTH, Settings.UNIT_LENGTH))


def drawBlackBlock(screen, loc):
    pygame.draw.rect(screen, Settings.BG_COLOR,
                     [loc[1] * Settings.UNIT_LENGTH,
                      loc[0] * Settings.UNIT_LENGTH,
                      Settings.UNIT_LENGTH,
                      Settings.UNIT_LENGTH])


def drawMoving(screen, figure, loc_last, loc_next, eat_dots=False):
    # 消去上一个格子
    if loc_next != loc_last:
        # EATING
        if Settings.TARGET_PACMAN == Settings.TARGET_EAT:
            drawBlackBlock(screen, loc_last)
        # ESCAPING
        elif Settings.TARGET_PACMAN == Settings.TARGET_ESCAPE:
            if eat_dots:
                drawBlackBlock(screen, loc_last)
            else:
                if Map.get((loc_last[0], loc_last[1])) == 0:
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
    ghost_1 = Ghost(10, 11, 'left')
    screen.blit(ghost_1.getFigure("./figures/red_right.png"), (11 * Settings.UNIT_LENGTH, 10 * Settings.UNIT_LENGTH))
    ghost_2 = Ghost(12, 13, 'left')
    screen.blit(ghost_1.getFigure("./figures/blue_right.png"), (13 * Settings.UNIT_LENGTH, 12 * Settings.UNIT_LENGTH))
    # 绘制pac-man
    pacman_1 = Pacman(11, 1, 'right')
    screen.blit(pacman_1.getFigure("./figures/Pacman_left.png"), (1 * Settings.UNIT_LENGTH, 11 * Settings.UNIT_LENGTH))
    # 让最近绘制的屏幕可见
    pygame.display.flip()

    loadMusic("./music/Devil Trigger.mp3")

    count_dots = 300
    # the main loop
    while True:
        # time interval among steps
        time.sleep(Settings.UNIT_INTERVAL)

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                break

        # current state
        state = {'ghost_locations': [ghost_1.getLoc(), ghost_2.getLoc()],
                 'pacman_location': pacman_1.getLoc()}

        # one move for pac-man&ghost
        # pac-man
        loc_last = pacman_1.getLoc()
        figure, loc_next = pacman_1.takeAction(state, Settings.ICONMAP_PACMAN)
        drawMoving(screen, figure, loc_last, loc_next, True)
        # eat a dot
        if Map.get(loc_next) == Settings.MAP_DOTS:
            Map.eatDots(loc_next)
            count_dots -= 1

        # gHost
        loc_last = ghost_1.getLoc()
        figure, loc_next = ghost_1.takeAction(state, Settings.ICONMAP_GHOST_1)
        drawMoving(screen, figure, loc_last, loc_next)

        loc_last = ghost_2.getLoc()
        figure, loc_next = ghost_2.takeAction(state, Settings.ICONMAP_GHOST_2)
        drawMoving(screen, figure, loc_last, loc_next)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

        # 判定胜利条件
        if ghost_1.getLoc() == pacman_1.getLoc() or ghost_2.getLoc() == pacman_1.getLoc():
            break
        if count_dots <= 0:
            break
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            break


if __name__ == '__main__':
    run_game()
