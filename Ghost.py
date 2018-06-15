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
import Map
import settings as Settings

class Ghost(Walker):
    # 这里的x, y为map数组里面的概念
    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)

    def evaluate(self, state):
        return 1;

    def getValueOfAction(self, loc, dir, state):
        shortestPath = Map.getShortestPath(Map.getNextLoc(loc, dir), state.get('pacman_location'))
        if shortestPath == 0:
            return Settings.MAX_VALUE
        else:
            return 100.0 / float(shortestPath)
