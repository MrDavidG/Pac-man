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
import Network

class Ghost(Walker):
    Count = 1
    model = Network()
    # 这里的x, y为map数组里面的概念
    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)
        self._no = Ghost.Count
        Ghost.Count += 1

    def getValueOfAction(self, loc, dir, state):
        start = Map.getNextLoc(loc, dir)
        if start == False:
            start = loc
        target = state.get('pacman_location')
        shortestPath = Map.getShortestPath(start, target)
        if shortestPath == 0:
            return Settings.MAX_VALUE
        else:
            return 100.0 / float(shortestPath)

    def predictAction(self, state):
        return Ghost.model.predict(state)
