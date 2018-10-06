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
import Map


class Pacman(Walker):

    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)

    def getNextAction(self):
        return 0, 0

    def evaluate(self, loc_next):
        return 0

    def getValueOfAction(self, loc, dir, state):
        start = Map.getNextLoc(loc, dir)
        if start == False:
            start = loc
        target = state.get('ghost_locations')[0]
        return float(Map.getShortestPath(start, target))  # 只有一个ghost的情况
