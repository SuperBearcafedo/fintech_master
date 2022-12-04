# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

from unit_step_func import np_unit_step
from sigmoid_func import sigmoid


def single_layer_neural_network(array_data, weight_data):
    return np.dot(array_data, weight_data)


if __name__ == "__main__":
    x = np.array([1, 2])
    w = np.array([[1, 3, 5], [2, 4, 6]])
    print(single_layer_neural_network(x, w))
