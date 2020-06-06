# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: load_figure.py
@time: 2019/1/20 2:08 PM

这一行开始写关于本文件的说明与解释
"""

import pygame
from config.config import ConfigReader

class FigureLoader:

    def __init__(self):
        self.__config = ConfigReader()
        self.__unit_length = self.__config.getConfig_int('default', 'unit_length')

        self.__path = '../data/figures/'

    def getFigure(self, figure):
        fig = pygame.image.load(self.__path + figure).convert_alpha()
        return pygame.transform.scale(fig, (self.__unit_length, self.__unit_length))

