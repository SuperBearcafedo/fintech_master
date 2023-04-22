# -*- coding: utf-8 -*-
import numpy as np
from activation_funcs.sigmoid_func import sigmoid
from activation_funcs.softmax_func import softmax


def numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)
    # 即遍历x的每个元素，生成其对应的偏导

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])  # 这里返回是的坐标，元素由multi_index表示
    while not it.finished:
        idx = it.multi_index
        print("正在计算{}的偏导".format(idx))
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 还原值
        it.iternext()  # 进入下次迭代

    # 下面硬解方法与上面的方法等价
    # if x.ndim == 1:
    #     for idx in range(x.shape[0]):
    #         print("正在计算(0,{})的偏导".format(idx))
    #         tmp_val = x[idx]
    #         x[idx] = float(tmp_val) + h
    #         fxh1 = f(x)  # f(x+h)
    #
    #         x[idx] = tmp_val - h
    #         fxh2 = f(x)  # f(x-h)
    #         grad[idx] = (fxh1 - fxh2) / (2 * h)
    #
    #         x[idx] = tmp_val  # 还原值
    # else:
    #     for idx in range(x.shape[0]):
    #         temp_sig = x[idx]
    #         for idy in range(len(temp_sig)):
    #             print("正在计算({},{})的偏导".format(idx, idy))
    #             tmp_val = (x[idx])[idy]
    #             (x[idx])[idy] = float(tmp_val) + h
    #             fxh1 = f(x)  # f(x+h)
    #
    #             (x[idx])[idy] = tmp_val - h
    #             fxh2 = f(x)  # f(x-h)
    #             (grad[idx])[idy] = (fxh1 - fxh2) / (2 * h)
    #
    #             (x[idx])[idy] = tmp_val  # 还原值

    return grad


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    #return -np.sum(t * np.log(y + 1e-7)) / batch_size
    return -np.sum(t*np.log(y[np.arange(batch_size), t] + 1e-7))/batch_size


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {"W1": weight_init_std * np.random.randn(input_size, hidden_size), "b1": np.zeros(hidden_size),
                       "W2": weight_init_std * np.random.randn(hidden_size, output_size), "b2": np.zeros(output_size)}

    def predict(self, x):
        W1, W2 = self.params["W1"], self.params["W2"]
        b1, b2 = self.params["b1"], self.params["b2"]

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy_var = np.sum(y == t) / float(x.shape[0])
        return accuracy_var

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_W, self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W, self.params["b1"])
        print("b1是:\n{}", self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W, self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W, self.params["b2"])

        return grads


if __name__ == "__main__":
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

