# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: class_pacman.py
@time: 2019/1/11 8:44 PM

这一行开始写关于本文件的说明与解释
"""

from service.service_figure import FigureService
from service.class_thread import Thread
from config.config import ConfigReader
from service.service_strategy import Strategy

from service.service_state import State


class Pacman(Thread):
    Num = 0

    def __init__(self, threadCond):
        super(Pacman, self).__init__(Pacman.Num, threadCond)
        self.__num = Pacman.Num
        Pacman.Num += 1

        self.__name = 'pacman'
        self.__dir = 'left'
        self.__x, self.__y = [(11, 1), (22, 11)][self.__num]
        self.__strategy = Strategy('PACMAN', ConfigReader.getConfig('setting', 'strategy'))

        # record the next action
        self.__x_next, self.__y_next = self.__x, self.__y
        self.__action = self.__dir

        self.__fig = FigureService()

    def getName(self):
        return self.__name

    def run(self):

        while True:
            # lock
            self.threadCond.acquire()

            # 如果地图还没有更新到最新的话
            while State.ready(self.__name):
                self.threadCond.wait()

            # choose action and temporally store it until all objs finish choosing
            self.__action, (self.__x_next, self.__y_next) = self.__strategy.next_step(self.getLoc())

            State.beReady(self.__name)

            self.threadCond.notifyAll()
            # release
            self.threadCond.release()

    def getFig(self):
        return self.__fig.getFig_pacman('Pacman_' + self.__dir + '.png')

    def getNextFig(self):
        if self.__action == 'stay':
            return self.__fig.getFig_pacman('Pacman_' + self.__dir + '.png')
        else:
            return self.__fig.getFig_pacman('Pacman_' + self.__action + '.png')

    def getLoc(self):
        return self.__x, self.__y

    def getNextLoc(self):
        return self.__x_next, self.__y_next

    def getFigAndLoc(self):
        return self.getFig(), self.__x, self.__y

    def go(self):
        # TODO: map端应该是先调用go，然后再进行画图
        # go
        self.__x, self.__y = self.__x_next, self.__y_next
        if self.__action != 'stay':
            self.__dir = self.__action
        # refresh
        self.__x_next, self.__y_next = None, None
        self.__action = None
