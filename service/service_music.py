# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_music.py
@time: 2019/1/11 8:45 PM

这一行开始写关于本文件的说明与解释
"""

from data.load_music import MusicPlayer

import pygame


class MusicService:

    def __init__(self):
        self.__music = MusicPlayer()

    def play(self):
        music = self.__music.getMusic()
        pygame.mixer.music.load('../data/music/' + music)
        pygame.mixer.music.play()
