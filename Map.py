#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Dawei Gao
@contact: david_gao@buaa.edu.cn
@software: PyCharm
@file: Map.py
@time: 2018/6/8 下午11:55

这里的(x, y)统一为数组概念上的序号，即纵轴方向为x，向下为正，横轴方向为y，向右为正

"""
import settings as Settings
import copy


def get((x, y)):
    return Settings.MAP[x][y]


def canReach((x, y)):
    return get((x, y)) in Settings.PATH


def getNextLoc(loc, dir, step=1):
    (x, y) = loc
    if dir == "right":
        y += step
    elif dir == "left":
        y -= step
    elif dir == "up":
        x -= step
    elif dir == "down":
        x += step
    if Settings.PASS_THROUGH:
        # 如果可以穿越的话
        (x, y) = (x % Settings.UNIT_HEIGHT, y % Settings.UNIT_WIDTH)
    else:
        # 如果不能穿越
        if x >= Settings.UNIT_HEIGHT or x < 0 or y >= Settings.UNIT_WIDTH or y <0:
            return loc
    if canReach((x, y)):
        return x, y
    else:
        return loc


def DepthFirst(target, path, threshold):
    if len(path)-1 >= threshold:
        return threshold + 1
    # 获得现在的位置
    (x, y) = path[-1]
    # end
    if (x, y) == target:
        return len(path)-1
    lengths = []
    # up
    path_ = copy.copy(path)
    loc_up = getNextLoc((x, y), "up")
    if canReach(loc_up) and loc_up not in path:
        path_.append(loc_up)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_down = getNextLoc((x, y), "down")
    if canReach(loc_down) and loc_down not in path:
        path_.append(loc_down)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_left = getNextLoc((x, y), "left")
    if canReach(loc_left) and loc_left not in path:
        path_.append(loc_left)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_right = getNextLoc((x, y), "right")
    if canReach(loc_right) and loc_right not in path:
        path_.append(loc_right)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
    # 返回长度最小的path
    if len(lengths) == 0:
        return Settings.LONGEST_LENGTH
    else:
        return min(lengths)


def Dijkstra(target, path):
    pass


def getShortestPath(start, target):
    if Settings.SHORTESTPATH_DF:
        shortestPath = DepthFirst(target, [start], Settings.LONGEST_LENGTH)
        return shortestPath
    else:
        return Dijkstra(target, [start])

DepthFirst((11, 0), [(10, 5)], Settings.LONGEST_LENGTH)