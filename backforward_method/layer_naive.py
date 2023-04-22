import copy
import numpy as np
from activation_funcs.softmax_func import softmax
from activation_funcs.two_layer_network import cross_entropy_error


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        # 在前向的过程中定义了xy的值，然后反向传播的时候是可以计算的
        self.x = x
        self.y = y
        output = x * y

        return output

    def backward(self, dout):
        # dout为下游传递的结果
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        output = x + y

        return output

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)  # 这里判断走到哪一条路径
        output = x.copy()  # 假定x是NumPy数组
        output[self.mask] = 0  # 将<=0的部分全部设置为0

        return output

    def backward(self, dout):
        dout[self.mask] = 0  # 将<=0的部分反向设置为0
        dx = dout

        return dx

class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1.0 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx


class Affine:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self. db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.w) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None  # softmax的输出
        self.t = None  # 监督数据

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:  # 监督数据是one-hot-vector的情况
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size

        return dx






