#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Dawei Gao
@contact: david_gao@buaa.edu.cn
@software: PyCharm
@file: Walker.py
@time: 2018/6/9 上午12:06


"""
import settings as Settings
import pygame


class Walker:

    def __init__(self, x, y, dir):
        self.__x = x
        self.__y = y
        self.__dir = dir
        self.__actions = ["right", "left", "up", "down", "stop"]

    def getLoc(self):
        return self.__x * Settings.UNIT_LENGTH, self.__y * Settings.UNIT_LENGTH

    def canReach(self, x, y):
        return Settings.MAP[x][y] in Settings.PATH

    def getNextLoc(self, dir, step=1):
        x, y = self.__x, self.__y
        if dir == "right":
            x += step
        elif dir == "left":
            x -= step
        elif dir == "up":
            y -= step
        elif dir == "down":
            y += step
        x, y = x % Settings.UNIT_WIDTH, y % Settings.UNIT_HEIGHT
        if self.canReach(x, y):
            return x, y
        else:
            return self.__x, self.__y

    def getFigure(self, figure):
        walker = pygame.image.load(figure).convert_alpha()
        return pygame.transform.scale(walker, (Settings.UNIT_LENGTH, Settings.UNIT_LENGTH))
