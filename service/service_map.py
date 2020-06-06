# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_map.py
@time: 2019/1/21 2:17 PM

这一行开始写关于本文件的说明与解释
"""
from config.config import ConfigReader
from data.load_map import MapLoader
from service.class_thread import Thread

import numpy as np
import queue
import copy


class MapService:
    # record present map
    __map = None

    @classmethod
    def initMap(cls):
        cls.__map = MapLoader().getMap()

    @classmethod
    def getInitializedMap(cls):
        return MapLoader().getMap()

    @classmethod
    def getPresentMap(cls):
        return cls.__map

    @classmethod
    def getLoc(cls, x, y):
        return cls.__map[x][y]

    @classmethod
    def eatDots(cls, x, y):
        cls.__map[x][y] = ConfigReader.getConfig_int('map', 'map_empty')

    @classmethod
    def isWall(cls, x, y):
        return cls.getLoc(x, y) == ConfigReader.getConfig_int('map', 'map_wall')

    @classmethod
    def getNextLoc(cls, loc, dir, step=1):
        x, y = loc
        [x_, y_] = np.array([x, y]) + np.array(ConfigReader.getConfig_array('action', dir))
        x_, y_ = (x_ % ConfigReader.getConfig_int('default', 'unit_height'),
                  y_ % ConfigReader.getConfig_int('default', 'unit_width'))
        if cls.isWall(x_, y_):
            return False
        else:
            return x_, y_

    @classmethod
    def getShortestPath(cls, loc_s, loc_t):
        x_s, y_s = loc_s
        x_t, y_t = loc_t
        if ConfigReader.getConfig('map', 'map_path_shortest') == 'bfs':
            return cls.__bfs(x_s, y_s, x_t, y_t)
        elif ConfigReader.getConfig('map', 'map_path_shortest') == 'dfs':
            return cls.__dfs([(x_s, y_s)], x_t, y_t, ConfigReader.getConfig_float('path', 'routh_bound_upper'))

    # breadth first
    @classmethod
    def __bfs(cls, x_s, y_s, x_t, y_t):
        state_processed = ConfigReader.getConfig_int('path', 'state_processed')
        state_untreated = ConfigReader.getConfig_array('path', 'state_untreated')
        state_pending = ConfigReader.getConfig_int('path', 'state_pending')

        # to be processed
        list_pending = queue.Queue()
        # queue: [(x, y, length),...]
        list_pending.put((x_s, y_s, 0))
        # record the path having been processed
        map_record = copy.copy(MapService.getInitializedMap())
        # loop
        while not list_pending.empty():
            (x, y, l) = list_pending.get()
            if (x, y) == (x_t, y_t):
                return l

            map_record[x][y] = state_processed
            for dir in ['up', 'down', 'left', 'right']:
                loc = cls.getNextLoc((x, y), dir)
                if loc == (x_t, y_t):
                    return l + 1
                # if not wall
                if loc != False and map_record[loc[0]][loc[1]] in state_untreated:
                    map_record[loc[0]][loc[1]] = state_pending
                    list_pending.put((loc[0], loc[1], l + 1))

    # deep first
    @classmethod
    def __dfs(cls, path, x_t, y_t, threshold):
        if len(path) - 1 >= threshold:
            return threshold + 1
        (x, y) = path[-1]
        # end
        if (x, y) == (x_t, y_t):
            return len(path) - 1
        lengths = []
        # up
        path_ = copy.copy(path)
        loc_up = cls.getNextLoc((x, y), "up")
        if loc_up == False:
            loc_up = (x, y)
        if loc_up not in path:
            path_.append(loc_up)
            length = cls.__dfs(path_, x_t, y_t, threshold)
            lengths.append(length)
            if length < threshold:
                threshold = length
            path_ = copy.copy(path)
        loc_down = cls.getNextLoc((x, y), "down")
        if loc_down == False:
            loc_down = (x, y)
        if loc_down not in path:
            path_.append(loc_down)
            length = cls.__dfs(path_, x_t, y_t, threshold)
            lengths.append(length)
            if length < threshold:
                threshold = length
            path_ = copy.copy(path)
        loc_left = cls.getNextLoc((x, y), "left")
        if loc_left == False:
            loc_left = (x, y)
        if loc_left not in path:
            path_.append(loc_left)
            length = cls.__dfs(path_, x_t, y_t, threshold)
            lengths.append(length)
            if length < threshold:
                threshold = length
            path_ = copy.copy(path)
        loc_right = cls.getNextLoc((x, y), "right")
        if loc_right == False:
            loc_right = (x, y)
        if loc_right not in path:
            path_.append(loc_right)
            length = cls.__dfs(path_, x_t, y_t, threshold)
            lengths.append(length)
            if length < threshold:
                threshold = length
        # return
        if len(lengths) == 0:
            return 99
        else:
            return min(lengths)
