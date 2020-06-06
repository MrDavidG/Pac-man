# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: service_strategy.py
@time: 2019/1/11 8:45 PM

这一行开始写关于本文件的说明与解释
"""

from keras.models import Sequential, load_model
from keras.layers import Dense
from service.service_map import MapService
from service.service_state import State

import numpy as np
import os


class Strategy:
    def __init__(self, role, strategy):
        # choose strategy according to the setting
        if strategy == 'GREEDY':
            self.__method = Greedy(role)
        elif strategy == 'RLEARNING':
            self.__method = RLearning(role)

    def next_step(self, loc):
        return self.__method.next(loc)


class Greedy:
    def __init__(self, role):
        self.role = role
        # record the func
        if role == 'PACMAN':
            self.__funcGetLoc = State.getGhostLocs
            self.__funcTarget = np.max
            self.__funcDecide = np.greater
        elif role == 'GHOST':
            self.__funcGetLoc = State.getPacLocs
            self.__funcTarget = np.min
            self.__funcDecide = np.less

    def next(self, loc):
        act_max, reward_max, loc_next_max = '', -1, None
        for act in ['left', 'right', 'up', 'down', 'stay']:
            # get next loc
            loc_next = MapService.getNextLoc(loc, act)
            if loc_next != False:
                reward_act = self.__funcTarget(
                    [MapService.getShortestPath(loc_next, loc_enemy) for loc_enemy in self.__funcGetLoc()])
                # get the max
                if self.__funcDecide(reward_act, reward_max) or reward_max == -1:
                    act_max, reward_max = act, reward_act
                    loc_next_max = loc_next
        return act_max, loc_next_max


class state:
    def __init__(self, state, action, reward, state_next):
        self.__state = state
        self.__action = action
        self.__reward = reward
        self.__state_next = state_next


class RLearning:
    def __init__(self, role):
        pass

    def DQN(self):
        M = 10
        T = 10
        epsilon = 0.5
        gamma = 0.5
        self.init_model()
        pool_experience = list()
        for i in range(M):
            # 初始化第一个state
            # TODO
            for j in range(T):
                if np.random.random() < epsilon:
                    # 随机进行一次
                    action = np.random.choice(['up', 'down', 'left', 'right', 'stay'])
                else:
                    # 选择预测的一次
                    action = self.predict(state)
                # 执行
                yield action
                # 获得下一个state_next, reward
                state_next, reward = 0, 0
                # 存储
                pool_experience += (state, action, reward, state_next)

                # 训练过程
                # 随机取出一些样本
                samples = np.random.choice(pool_experience, min(100, len(pool_experience)))
                # 打标签
                labels = []
                for sample in samples:
                    if sample == '终结状态':
                        label = reward
                    else:
                        # 首先要获取到
                        label = reward + gamma * max(self.predict(state, action))  # !!!!
                    labels += [label]
                self.__model.train_on_batch(samples, labels)

    def init_model(self, path='./model.hdf5'):
        if os.path.exists(path):
            self.__model = load_model(path)
        else:
            self.__model = Sequential(Dense(3, activation='relu'),
                                      Dense(100, activation='relu'),
                                      Dense(100, activation='relu'),
                                      Dense(5, activation='softmax'))
            self.__model.compile(optimizer='amda',
                                 metrics=['mae'],
                                 loss='mae')

    def predict(self, x):
        actions = self.__model.predict([x])[0]

    def saveModel(self, path='./model.hdf5'):
        self.__model.save(path)
