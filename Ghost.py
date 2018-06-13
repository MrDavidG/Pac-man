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
        self.__iconMap = {'right': './figures/red_right.png',
                          'left': './figures/red_left.png',
                          'up': './figures/red_up.png',
                          'down': './figures/red_down.png'}

    def greedy(self, x, y):
        for action in self.__action:
            print action

    def evaluate(self, action):
        return 1;
