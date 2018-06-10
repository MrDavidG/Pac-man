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
import Walker


class Ghost(Walker):

    def __init__(self, x, y):
        Walker.__init__(self, x, y)
        self.__icon_right = "./figure/ghost_right.png"
        self.__icon_left = "./figures/ghost_left.png"
        self.__icon_up = "./figures/ghost_up.png"
        self.__icon_down = "./figures/ghost_down.png"

    def greedy(self, x, y):
        for action in self.__action:
            print action

    def chase(self, x, y):
        pass


if __name__ == "__main__":
    a = Ghost(1,3)