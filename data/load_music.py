# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_music.py
@time: 2019/1/18 2:44 PM

这一行开始写关于本文件的说明与解释
"""

from config.config import ConfigReader

import os
import numpy as np


class MusicPlayer:

    def getMusic(self):
        return np.random.choice([_ for _ in os.listdir('../data/music') if _.endswith('.mp3')])
