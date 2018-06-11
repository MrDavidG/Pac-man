#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Dawei Gao
@contact: david_gao@buaa.edu.cn
@software: PyCharm
@file: Pacman.py
@time: 2018/6/8 下午11:34


"""
from Walker import Walker
import numpy as np


class Pacman(Walker):

    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)
        self.__iconMap = {'right': '/figures/Pacman_right.png',
                          'left': './figures/Pacman_left.png',
                          'ip': './figures/Pacman_up.png',
                          'down': './figures/Pacman_down.png'}

    def getNextAction(self):
        return 0, 0,

    def evaluate(self, state):
        return 0

    def takeAction(self, state):
        actions = {'left': 0,
                   'right': 0,
                   'up': 0,
                   'down': 0,
                   'stop': 0}
        # 获取所有actions在当前state下的value
        for key in actions:
            loc_next = self.getNextLoc(key)
            actions[key] = self.evaluate(state, loc_next)
        argmax_key = np.argmax(actions)
        # TODO: 如果有ties需要解决

        return self.__iconMap[argmax_key], self.getNextLoc(argmax_key)
