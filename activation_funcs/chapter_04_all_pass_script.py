from dataset.mnist import load_mnist
import numpy as np
from two_layer_network import TwoLayerNet
import matplotlib.pylab as plt

if __name__ == "__main__":
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

    # 训练损失，放在一个数组中
    train_loss_list = []

    # 设定一系列超参数
    iters_num = 10000  # 设置迭代次数
    train_size = x_train.shape[0]  # 读取训练集的第一维大小
    print(train_size)
    batch_size = 100  # 每批次的大小
    learning_rate = 0.1  # 每次收敛的步长
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
    for i in range(iters_num):
        print("已经第{}次!".format(i))
        # 获取每次得到的mini_batch
        batch_mask = np.random.choice(train_size, batch_size)  # 从60000中随机选取100个，作为一批次
        x_batch = x_train[batch_mask]  # 测试的批次
        t_batch = t_train[batch_mask]  # 对应批次的结果
        print("正在计算梯度！")
        grad = network.numerical_gradient(x_batch, t_batch)  # 得到梯度矩阵

        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate*grad[key]

        # 损失函数
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

    # 作图
    for i in range(len(train_loss_list)):
        plt.plot(i, train_loss_list[i])
        plt.show()


