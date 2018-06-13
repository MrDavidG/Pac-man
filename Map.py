#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Dawei Gao
@contact: david_gao@buaa.edu.cn
@software: PyCharm
@file: Map.py
@time: 2018/6/8 下午11:55


"""
import settings as Settings


def canReach(self, x, y):
    return Settings.MAP[x][y] in Settings.PATH


def getNextLoc(self, loc, dir, step=1):
    (x, y) = loc
    if dir == "right":
        x += step
    elif dir == "left":
        x -= step
    elif dir == "up":
        y -= step
    elif dir == "down":
        y += step
    x, y = x % Settings.UNIT_WIDTH, y % Settings.UNIT_HEIGHT
    if self.canReach(x, y):
        return x, y
    else:
        return self.__x, self.__y


def DepthFirst(target, path):
    # 获得现在的位置
    (x, y) = path[len(path) - 1]
    # end
    if (x, y) == target:
        return len(path)
    lengths = {}
    # up
    path_ = path
    loc_up = getNextLoc((x, y), "up")
    if canReach(loc_up) and loc_up not in path:
        lengths["up"] = DepthFirst(target, path_.append(loc_up))
        path_ = path
    loc_down = getNextLoc((x, y), "down")
    if canReach(loc_down) and loc_down not in path:
        lengths["down"] = DepthFirst(target, path_.append(loc_down))
        path_ = path
    loc_left = getNextLoc((x,y), "left")
    if canReach(loc_left) and loc_left not in path:
        lengths["left"] = DepthFirst(target, path_.append(loc_left))
        path_ = path
    loc_right = getNextLoc((x,y), "right")
    if canReach(loc_right) and loc_right not in path:
        lengths["right"] = DepthFirst(target, path_.append(loc_right))
    argmin_key = min(lengths, key=lengths.get)
    return min(lengths)



def Dijkstra(target, path):
    pass


def getShortestPath(start, target):
    if Settings.SHORTESTPATH_DF:
        return DepthFirst(target, [start])
    else:
        return Dijkstra(target, [start])
