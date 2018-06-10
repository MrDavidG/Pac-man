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
import Walker


class Pacman(Walker):

    def __init__(self, x, y):
        super(Pacman, self).__init__(x, y)
        self.__icon_right = "./figures/Pacman_right.png"
        self.__icon_left = "./figures/Pacman_left.png"
        self.__icon_up = "./figures/Pacman_up.png"
        self.__icon_down = "./figures/Pacman_down.png"

    def getNextAction(self):
        return 0, 0

    def evaluate(self, ):
        pass

    def go(self):
        # evaluate
        x_next, y_next = self.getNextAction()
        icon = self.getFigure(self.__icon_right)
        return x_next, y_next, icon
