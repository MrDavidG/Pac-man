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
import random

class Walker:

    def __init__(self, x, y, dir):
        self.__x = x
        self.__y = y
        self.__dir = dir
        self.__actions = ["right", "left", "up", "down", "stop"]

    def getLoc(self):
        return self.__x, self.__y




    def getArcMax_key(self, dict):
        max_ = max(dict.values())
        list = []
        for key in dict.keys():
            if dict.get(key)==max_:
                list.append(key)
        res_index = random.randrange(0, len(list))
        return list[res_index]

    def getFigure(self, figure):
        walker = pygame.image.load(figure).convert_alpha()
        return pygame.transform.scale(walker, (Settings.UNIT_LENGTH, Settings.UNIT_LENGTH))

    def takeAction(self, state):
        actions = {'left': 0,
                   'right': 0,
                   'up': 0,
                   'down': 0,
                   'stop': 0}
        # 获取所有actions在当前state下的value
        for key in actions:
            loc_next = self.getNextLoc(key)
            actions[key] = self.evaluate(loc_next)
        argmax_key = self.getArgMax_key(actions)
        return self.__iconMap.get(argmax_key), self.getNextLoc(argmax_key)
