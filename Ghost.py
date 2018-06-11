#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Dawei Gao
@contact: david_gao@buaa.edu.cn
@software: PyCharm
@file: Ghost.py
@time: 2018/6/8 下午11:34


"""
from Walker import Walker
import numpy as np


class Ghost(Walker):

    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)
        self.__iconMap = {'right': './figures/ghost_right.png',
                          'left': './figures/ghost_left.png',
                          'up': './figures/ghost_up.png',
                          'down': './figures/ghost_down.png'}

    def greedy(self, x, y):
        for action in self.__action:
            print action

    def evaluate(self, action):
        return 0;

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

        argmax_key = np.argmax(actions)
        # TODO: 如果有ties需要解决

        return self.__iconMap[argmax_key], self.getNextLoc(argmax_key, argmax_key)


if __name__ == "__main__":
    a = Ghost(1, 3)
