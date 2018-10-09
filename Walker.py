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
import Map
import numpy as np


class Walker:

    def __init__(self, x, y, dir):
        self.__x = x
        self.__y = y
        self.__dir = dir
        self.__actions = ["right", "left", "up", "down", "stop"]
        self.__iconMap = {}

    def getLoc(self):
        return self.__x, self.__y

    def getArcMax_key(self, dict):
        max_ = max(dict.values())
        list = []
        for key in dict.keys():
            if dict.get(key) == max_:
                list.append(key)
        res_index = random.randrange(0, len(list))
        return list[res_index]

    def getFigure(self, figure):
        walker = pygame.image.load(figure).convert_alpha()
        return pygame.transform.scale(walker, (Settings.UNIT_LENGTH, Settings.UNIT_LENGTH))

    def getValueOfAction(self, loc, dir, state):
        pass

    def Greedy(self, state, iconMap):
        valuesOfActions = {'left': 0,
                           'right': 0,
                           'up': 0,
                           'down': 0,
                           'stay': 0}
        loc = (self.__x, self.__y)
        # 获取所有actions在当前state下的value
        for key in valuesOfActions:
            valuesOfActions[key] = self.getValueOfAction(loc, key, state)
        argmax_dir = self.getArcMax_key(valuesOfActions)
        loc_temp = Map.getNextLoc(loc, argmax_dir)
        if loc_temp == False:
            (self.__x, self.__y) = loc
        else:
            (self.__x, self.__y) = loc_temp
        return iconMap.get(argmax_dir), (self.__x, self.__y)

    def predictAction(self, state):
        pass

    def trainModel(self, data, label):
        pass

    def getEnvVec(self):
        # TODO

        return Map.Map

    def getActionVec(self, dir):
        vec = np.zeros(5)
        vec[Settings.QLEARNING_DICT[dir]] = 1
        return vec

    def QLearning(self, state, iconMap):
        threshold = Settings.QLEARNING_THRESHOLD
        if random.random() > threshold:
            # random pick an feasible action
            actions_feasible = Map.getFeasibleActions((self.__x, self.__y))
            dir = random.choice(actions_feasible)
            if dir == 'stay':
                return (self.__x, self.__y)
            else:
                loc = (self.__x, self.__y)
                loc_temp = Map.getNextLoc(loc, dir)
                if loc_temp != False:
                    (self.__x, self.__y) = loc_temp
                # train NN
                # TODO 有问题，dir到底应该是要真实的才对
                self.trainModel(self.getEnvVec(), self.getActionVec(dir))
                return iconMap.get(dir), (self.__x, self.__y)
        else:
            # predict through the neural network
            # 通过函数调用来把行为上调成上一层的接口
            self.predictAction(state)

    def takeAction(self, state, iconMap):
        if Settings.STRATEGY_GAME == Settings.STRATEGY_GREEDY:
            return self.Greedy(state, iconMap)
        elif Settings.STRATEGY_GAME == Settings.STRATEGY_QLEARNING:
            return self.QLearning(state, iconMap)
