# encoding: utf-8
"""
@author:    dawei gao
@contact:   david_gao@buaa.edu.cn

@version: 1.0
@license: Apache Licence
@file: Network.py
@time: 2018/10/8 下午4:45

use to
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Network:
    def __init__(self):
        self.__model = Sequential()
        self.__model.add(Dense(3, activation="relu", input_dim=2))
        self.__model.add(Dense(5, activation="sigmoid"))
        self.__model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])

    def predict(self, data):
        return self.__model.predict(data)

    def training(self, data, label):
        self.__model.train_on_batch(data, label)

    def saveModel(self, path='./model.hdf5'):
        self.__model.save(path)

# 生成dummy data
# data = np.random.random((1000, 2))
# labels = np.random.random((1000,1))
data = np.array([[1, 2], [3, 4]])
labels = np.array([[1],[2]])