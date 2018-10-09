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
import Network


class Pacman(Walker):
    Count = 1
    model = Network()

    def __init__(self, x, y, dir):
        Walker.__init__(self, x, y, dir)
        self._no = Pacman.Count
        Pacman.Count += 1

    def getValueOfAction(self, loc, dir, state):
        start = Map.getNextLoc(loc, dir)
        if start == False:
            start = loc
        list_dis = []
        for ghost_location in state.get('ghost_locations'):
            list_dis += [float(Map.getShortestPath(start, ghost_location))]
        return min(list_dis)

    def predictAction(self, state):
        return Pacman.model.predict(state)
