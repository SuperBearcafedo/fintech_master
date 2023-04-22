# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

from activation_funcs.unit_step_func import np_unit_step
from activation_funcs.sigmoid_func import sigmoid


def softmax_basic(np_array):
    """
    这样实现存在溢出风险，当每个x都接近无穷大，计算机算出的全是Inf，计算结果都是不确定的
    :param np_array:
    :return:
    """
    exp_array = np.exp(np_array)
    sum_exp_array = np.sum(exp_array)
    result = exp_array / sum_exp_array
    return result


def softmax(np_array):
    """
    其实仍然存在缺陷在于当首尾分布相差过大时，仍然无法防止溢出 ToDo：需要进一步解决
    :param np_array:
    :return:
    """
    max_num = np.max(np_array)
    exp_array = np.exp(np_array - max_num)
    sum_exp_array = np.sum(exp_array)
    result = exp_array / sum_exp_array
    return result


if __name__ == "__main__":
    x = np.arange(-5.0, 5, 0.1)
    y = softmax(x)

    #plt.plot(x, y)
    #plt.show()
