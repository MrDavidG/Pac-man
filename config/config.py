# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: config.py
@time: 2019/1/18 4:29 PM

这一行开始写关于本文件的说明与解释
"""

import configparser
import json


class ConfigReader:
    cf = configparser.ConfigParser()

    @classmethod
    def loadConfig(cls):
        cls.cf.read('../config/config.ini')

    @classmethod
    def getConfig(cls, section, option):
        return cls.cf.get(section, option)

    @classmethod
    def getConfig_int(cls, section, option):
        return cls.cf.getint(section, option)

    @classmethod
    def getConfig_float(cls, section, option):
        return cls.cf.getfloat(section, option)

    @classmethod
    def getConfig_array(cls, section, option):
        return json.loads(cls.cf.get(section, option).replace('\'', '\"'))
