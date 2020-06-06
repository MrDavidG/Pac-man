# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: class_thread
@time: 2020/6/4 1:13 上午

Description. 
"""

import threading
import time

import abc


class Thread(threading.Thread):
    def __init__(self, threadID, threadCond):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadCond = threadCond

    @abc.abstractmethod
    def run(self):
        pass
