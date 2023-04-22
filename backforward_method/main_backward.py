from collections import OrderedDict
import matplotlib.pylab as plt

import numpy as np
from activation_funcs.unit_step_func import np_unit_step
from activation_funcs.sigmoid_func import sigmoid
from activation_funcs.common_funcs import homo_list_length, compare_list_element
from dataset.mnist import load_mnist
from layer_naive import Affine, Relu, SoftmaxWithLoss


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
    return grad


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    # x:输入数据, t:监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1: t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    # x:输入数据, t:监督数据
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads

    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dw, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dw, self.layers['Affine2'].db

        return grads


if __name__ == '__main__':
    # '''
    # 此部分仅仅模拟计算苹果的过程
    # '''
    # apple = 100
    # apple_num = 2
    # tax = 1.1
    #
    # mul_apple_layer = MulLayer()
    # mul_tax_layer = MulLayer()
    #
    # # 计算前向的结果
    # apple_price = mul_apple_layer.forward(apple, apple_num)
    # price = mul_tax_layer.forward(apple_price, tax)
    # print(price)
    #
    # # 计算后向的结果
    # dprice = 1
    # dapple_price, dtax = mul_tax_layer.backward(dprice)
    # dapple, dapple_num = mul_apple_layer.backward(dapple_price)
    # print(dapple, dapple_num, dtax)

    # '''
    # 此部分仅仅模拟计算苹果+橘子的过程
    # '''
    # apple = 100
    # apple_num = 2
    # orange = 150
    # orange_num = 3
    # tax = 1.1
    #
    # mul_apple_layer = MulLayer()
    # mul_orange_layer = MulLayer()
    # add_apple_orange_layer = AddLayer()
    # mul_tax_layer = MulLayer()
    #
    # # 模拟前向运算
    # apple_price = mul_apple_layer.forward(apple, apple_num)
    # orange_price = mul_orange_layer.forward(orange, orange_num)
    # all_price = add_apple_orange_layer.forward(apple_price, orange_price)
    # price = mul_tax_layer.forward(all_price, tax)
    #
    # # 模拟反向运算
    # dprice = 1
    # dall_price, dtax = mul_tax_layer.backward(dprice)
    # dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
    # dapple, dapple_num = mul_apple_layer.backward(dapple_price)
    # dorange, dorange_num = mul_orange_layer.backward(dorange_price)
    #
    # print(price)
    # print(dapple_num, dapple_price, dorange_num, dorange_price, dapple, dorange, dtax)

    """
    下面计算利用反向传播法的学习过程
    """
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    iters_num = 1000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_per_epoch = max(train_size / batch_size, 1)

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 梯度
        # grad = network.numerical_gradient(x_batch, t_batch)
        grad = network.gradient(x_batch, t_batch)

        # 更新
        for key in ('W1', 'b1', 'W2', 'b2'):
            if grad[key].shape == network.params[key].shape:
                print("大小相等")
                network.params[key] -= learning_rate * grad[key]
            else:
                print("大小不等!!!!!!!!", grad[key].shape, network.params[key].shape)

        # 损失函数
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
    print(train_loss_list)

    # # 作图
    # for i in range(len(train_loss_list)):
    plt.plot(train_loss_list)
    plt.show()
