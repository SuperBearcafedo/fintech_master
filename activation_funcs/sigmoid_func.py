# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

from unit_step_func import np_unit_step


def sigmoid(np_array):
    return 1 / (1 + np.exp(-np_array))


if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)
    plt.ylim(-0.1, 1)

    fig, ax = plt.subplots()
    y1 = y
    ax.plot(x, y1, label="sigmoid")
    y2 = np_unit_step(x)
    ax.plot(x, y2, label="unit step")
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_title("Comparisons Between Sigmoid and Unit Step")
    ax.legend()
    plt.show()

