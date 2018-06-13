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


class Pacman(Walker):

    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)
        self.__iconMap = {'right': '/figures/Pacman_right.png',
                          'left': './figures/Pacman_left.png',
                          'ip': './figures/Pacman_up.png',
                          'down': './figures/Pacman_down.png'}

    def getNextAction(self):
        return 0, 0,

    def evaluate(self, loc_next):
        return 0


