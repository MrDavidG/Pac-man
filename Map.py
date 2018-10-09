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
import Queue

Map = copy.copy(Settings.MAP)


def get((x, y)):
    return Map[x][y]


def eatDots((x, y)):
    Map[x][y] = Settings.MAP_EMPTY


def canReach((x, y)):
    return get((x, y)) in Settings.MAP_PATH


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
        if x >= Settings.UNIT_HEIGHT or x < 0 or y >= Settings.UNIT_WIDTH or y < 0:
            return loc
    if canReach((x, y)):
        return x, y
    else:
        return False


def getFeasibleActions(loc, step=1):
    actions_feasible = ['stay']
    for dir in ['up', 'down', 'left', 'right']:
        if getNextLoc(loc, 'up') != False:
            actions_feasible += [dir]
    return actions_feasible


def BreadthFirst(start, target):
    # 记录当前待处理的节点
    list_pending = Queue.Queue()
    # 初始化，把起点变成待处理状态
    list_pending.put((start[0], start[1], 0))
    # 用来记录已经遍历过的节点
    map_record = copy.copy(Settings.MAP)
    # 开始循环处理所有待处理的节点
    while not list_pending.empty():
        (x, y, l) = list_pending.get()
        if (x, y) == target:
            # 返回路径长度
            return l
        # 变为已经处理
        map_record[x][y] = Settings.STATE_PROCESSED
        for dir in ['up', 'down', 'left', 'right']:
            loc = getNextLoc((x, y), dir)
            # 不撞墙
            if loc != False:
                # 没有遍历过
                if map_record[loc[0]][loc[1]] in Settings.STATE_UNTREATED:
                    map_record[loc[0]][loc[1]] = Settings.STATE_PENDING
                    list_pending.put((loc[0], loc[1], l + 1))


def DepthFirst(target, path, threshold):
    if len(path) - 1 >= threshold:
        return threshold + 1
    # 获得现在的位置
    (x, y) = path[-1]
    # end
    if (x, y) == target:
        return len(path) - 1
    lengths = []
    # up
    path_ = copy.copy(path)
    loc_up = getNextLoc((x, y), "up")
    if loc_up == False:
        loc_up = (x, y)
    if canReach(loc_up) and loc_up not in path:
        path_.append(loc_up)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_down = getNextLoc((x, y), "down")
    if loc_down == False:
        loc_down = (x, y)
    if canReach(loc_down) and loc_down not in path:
        path_.append(loc_down)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_left = getNextLoc((x, y), "left")
    if loc_left == False:
        loc_left = (x, y)
    if canReach(loc_left) and loc_left not in path:
        path_.append(loc_left)
        length = DepthFirst(target, path_, threshold)
        lengths.append(length)
        if length < threshold:
            threshold = length
        path_ = copy.copy(path)
    loc_right = getNextLoc((x, y), "right")
    if loc_right == False:
        loc_right = (x, y)
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
    if Settings.SHORTESTPATH_BFS:
        return BreadthFirst(start, target)
    elif Settings.SHORTESTPATH_DF:
        return DepthFirst(target, [start], Settings.LONGEST_LENGTH)
    elif Settings.SHORTESTPATH_DIJ:
        return Dijkstra(target, [start])
