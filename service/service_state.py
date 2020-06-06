# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_state
@time: 2020/6/4 3:54 下午

Record all objs to obtain their locations.
"""

import numpy as np


class State:
    __pacs = None
    __ghosts = None
    __dict = None

    @classmethod
    def initState(cls, pacs, ghosts):
        cls.__pacs = pacs
        cls.__ghosts = ghosts
        cls.__dict = dict()
        for obj in pacs + ghosts:
            cls.__dict[obj.getName()] = False

    @classmethod
    def beReady(cls, name):
        # 通知系统自己已经准备好了
        cls.__dict[name] = True

    @classmethod
    def ready(cls, name):
        # 查询自己是否ready，如果已经ready的话就wait
        return cls.__dict[name]

    @classmethod
    def allReady(cls):
        if sum(cls.__dict.values()) == len(cls.__pacs + cls.__ghosts):
            # 所有人都准备好了
            for obj in cls.__pacs + cls.__ghosts:
                cls.__dict[obj.getName()] = False
            return False
        else:
            return True

    @classmethod
    def getPacLocs(cls):
        return [_.getLoc() for _ in cls.__pacs]

    @classmethod
    def getGhostLocs(cls):
        return [_.getLoc() for _ in cls.__ghosts]

    @classmethod
    def getPacs(cls):
        return cls.__pacs

    @classmethod
    def getGhosts(cls):
        return cls.__ghosts

    @classmethod
    def getObjs(cls):
        return cls.__pacs + cls.__ghosts
