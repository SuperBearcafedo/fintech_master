# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

from unit_step_func import np_unit_step
from sigmoid_func import sigmoid


def relu(np_array):
    return np.maximum(0, np_array)


if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)

    fig, ax = plt.subplots()
    y1 = y
    ax.plot(x, y1, label="sigmoid")
    y2 = np_unit_step(x)
    ax.plot(x, y2, label="unit step")
    y3 = relu(x)
    ax.plot(x, y3, label="rectified linear unit")
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_title("Comparisons Between Sigmoid and Unit Step")
    ax.legend()
    plt.show()

