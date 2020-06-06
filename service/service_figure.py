# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: load_figure.py
@time: 2019/1/21 11:10 AM

这一行开始写关于本文件的说明与解释
"""

from data.load_figure import FigureLoader


class FigureService:

    def __init__(self):
        self.__figLoader = FigureLoader()

    def getFig_pacman(self, name):
        return self.__figLoader.getFigure(name)

    def getFig_ghost(self, name):
        return self.__figLoader.getFigure(name)

    def getFig_wall(self):
        return self.__figLoader.getFigure('wall.png')

    def getFig_dot(self):
        return self.__figLoader.getFigure('path_dot.png')

    def getFig_path(self):
        return self.__figLoader.getFigure('path_black.png')
