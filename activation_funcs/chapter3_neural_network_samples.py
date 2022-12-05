# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

from unit_step_func import np_unit_step
from sigmoid_func import sigmoid


def single_layer_neural_network(array_data, weight_data):
    return np.dot(array_data, weight_data)


def identity_function(array_data):
    return array_data


if __name__ == "__main__":
    # 实现P55 图3-14 神经网络的内积
    x = np.array([1, 2])
    w = np.array([[1, 3, 5], [2, 4, 6]])
    print(single_layer_neural_network(x, w))

    # P59 图3-17的第一层神经网络
    x2 = np.array([1.0, 0.5])
    w2 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b2 = np.array([0.1, 0.2, 0.3])

    A1 = np.dot(x2, w2) + b2
    Z1 = sigmoid(A1)  # 第一层运行完，进行激活判断
    print("第一层神经元输出结果为：", Z1)

    # P60 图3-18的第二层神经网络
    w3 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    b3 = np.array([0.1, 0.2])

    A2 = np.dot(Z1, w3) + b3
    Z2 = sigmoid(A2)
    print("第二层神经元输出结果为：", Z2)

    w4 = np.array([[0.1, 0.3], [0.2, 0.4]])
    b4 = np.array([0.1, 0.2])

    A3 = np.dot(Z2, w4) + b4
    Y = identity_function(A3)
    print("第三层神经元输出结果为：", Y)
