# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: ui_interface.py
@time: 2019/1/11 7:39 PM

这一行开始写关于本文件的说明与解释
"""

import pygame
from config.config import ConfigReader
from service.service_figure import FigureService
from service.class_thread import Thread
from service.service_map import MapService
from service.service_state import State


class Interface():
    def __init__(self):

        self.__config = ConfigReader()
        self.__screen_width = self.__config.getConfig_int('default', 'screen_width')
        self.__screen_height = self.__config.getConfig_int('default', 'screen_height')
        self.__unit_length = self.__config.getConfig_int('default', 'unit_length')
        self.__unit_width = self.__config.getConfig_int('default', 'unit_width')
        self.__unit_height = self.__config.getConfig_int('default', 'unit_height')

        self.__screen = None

        self.__fig = None
        self.__wall = None
        self.__path_dot = None
        self.__path_black = None

        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

        self.__fig = FigureService()
        self.__wall = self.__fig.getFig_wall()
        self.__path_dot = self.__fig.getFig_dot()
        self.__path_black = self.__fig.getFig_path()

    def initialize(self):
        pygame.display.set_caption("Catch Me If You CAN")

        # draw screen
        # background
        self.__screen.fill((0, 0, 0))
        # draw map
        for i in range(self.__unit_height):
            for j in range(self.__unit_width):
                if (MapService.getLoc(i, j) == 1):
                    self.__screen.blit(self.__wall, (j * self.__unit_length, i * self.__unit_length))
                elif (MapService.getLoc(i, j) == 0):
                    self.__screen.blit(self.__path_dot, (j * self.__unit_length, i * self.__unit_length))

        pygame.display.flip()

    def draw_object(self, x, y, fig):
        self.__screen.blit(fig, (y * self.__unit_length, x * self.__unit_length))

    def draw_pac_move(self, fig, loc_last, loc_next):
        # erase last loc
        self.__screen.blit(self.__path_black, (loc_last[1] * self.__unit_length, loc_last[0] * self.__unit_length))
        # go forward and eat dot (if it has)
        self.__screen.blit(fig, (loc_next[1] * self.__unit_length, loc_next[0] * self.__unit_length))
        MapService.eatDots(loc_next[0], loc_next[1])

    def draw_ghost_move(self, fig, loc_last, loc_next):
        # erase last loc
        path_before = MapService.getLoc(loc_last[0], loc_last[1])
        if path_before == ConfigReader.getConfig_int('map', 'map_empty'):
            fig_path = self.__path_black
        elif path_before == ConfigReader.getConfig_int('map', 'map_dots'):
            fig_path = self.__path_dot
        self.__screen.blit(fig_path, (loc_last[1] * self.__unit_length, loc_last[0] * self.__unit_length))
        # go forward and eat dot (if it has)
        self.__screen.blit(fig, (loc_next[1] * self.__unit_length, loc_next[0] * self.__unit_length))

    def flip(self):
        pygame.display.flip()
