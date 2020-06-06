# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_game.py.py
@time: 2019/1/11 8:44 PM

这一行开始写关于本文件的说明与解释
"""

from ui.ui_interface import Interface
from config.config import ConfigReader
from service.service_music import MusicService
from service.service_map import MapService
from service.service_figure import FigureService
from service.class_pacman import Pacman
from service.class_ghost import Ghost
from service.service_state import State

import threading
import pygame
import time
import sys


class PacGame:

    def __init__(self):
        # init config
        ConfigReader.loadConfig()
        # init map
        MapService.initMap()

        # thread lock
        self.__condition = threading.Condition()

        # init service
        pygame.init()
        self.__music = MusicService()
        self.__fig = FigureService()
        self.__interface = Interface()

        # init objs
        State.initState([Pacman(self.__condition)], [Ghost(self.__condition), Ghost(self.__condition)])

    def run(self):
        # music
        # self.__music.play()

        MapService.getShortestPath((11, 0), (10, 11))

        # draw map
        # self.__interface.initialize()
        # draw pac & ghost
        # TODO: these should be down in ui_interface
        # for pac in self.__pacs:
        #     fig, x, y = pac.getFigAndLoc()
        #     self.__interface.draw_object(x, y, fig)
        # for ghost in self.__ghosts:
        #     fig, x, y = ghost.getFigAndLoc()
        #     self.__interface.draw_object(x, y, fig)

        self.__interface.initialize()

        # num of dots
        count_dots = 300
        # create new threads
        # TODO: 理想状态应该是为每一个object创建一个新线程,启动所有的线程
        for obj in State.getObjs():
            obj.start()
        # # wait until game ends
        # for obj in State.getObjs():
        #     obj.join()

        # main loop
        while True:
            self.__condition.acquire()

            while State.allReady():
                self.__condition.wait()

            # 画下一步
            for pac in State.getPacs():
                self.__interface.draw_pac_move(pac.getNextFig(), pac.getLoc(), pac.getNextLoc())

            for ghost in State.getGhosts():
                self.__interface.draw_ghost_move(ghost.getNextFig(), ghost.getLoc(), ghost.getNextLoc())

            # 然后再走这一步，走的时候要进行eat操作
            for obj in State.getObjs():
                obj.go()

            self.__interface.flip()

            self.__condition.notifyAll()
            # release
            self.__condition.release()

            # time.sleep(0.2)

            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    break

        # # main loop
        # while True:
        #     # time intervals
        #     time.sleep(ConfigReader.getConfig_float('default', 'unit_interval'))
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #         else:
        #             break
        #
        #     # take actions
        #     # 怎么做到同步！！！
        #     for pac in self.__pacs:
        #         pac.go()
        #     for ghost in self.__ghosts:
        #         ghost.go()
        #
        #     # draw
        #
        #     # refresh
        #     self.__interface.flip()
        #
        #     # victory


if __name__ == '__main__':
    # play
    game = PacGame()
    game.run()
