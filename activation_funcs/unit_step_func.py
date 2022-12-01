# -*- coding: utf-8 -*-

from common_funcs import homo_list_length, compare_list_element

"""
    python常用的三个类型函数判定：
    type() 返回参数的数据类型
    dtype() 返回数组中元素的数据类型
    astype() 对数据类型进行转换
"""


def unit_step(value, threshold):
    """
    1.实现对list类型的阶跃函数响应
    2.实现对int/float等单个类型的阶跃函数响应
    :param value:
    :param threshold:
    :return:
    """
    if type(value) == list and type(threshold) == list:
        l1, l2 = homo_list_length(value, threshold)
        return compare_list_element(l1, l2)
    elif type(value) == list and type(threshold) != list:
        threshold_temp = [threshold]
        l1, l2 = homo_list_length(value, threshold_temp)
        return compare_list_element(l1, l2)
    elif type(value) != list and type(threshold) == list:
        value_temp = [value]
        l1, l2 = homo_list_length(value_temp, threshold)
        return compare_list_element(l1, l2)
    else:
        if value >= threshold:
            return 1
        return 0


def anti_unit_step(value, threshold):
    """
    实现对unit_step阶跃函数结果的取反-->响应
    :param value:
    :param threshold:
    :return:
    """
    result = []
    unit_step_result = unit_step(value, threshold)
    if type(unit_step_result) == list:
        for element in unit_step_result:
            if element == 1:
                result.append(0)
            else:
                result.append(1)
        return result
    if unit_step_result == 1:
        return 0
    return 1


# ToDo：返回的节约函数结果的元素类型应该一致，比如int全部转化为int,float全部转化为float


if __name__ == "__main__":
    print(unit_step(1, 2))  # 实例1
    print(unit_step([1, -1], 2))  # 实例2
    print(unit_step(1, [-1, 100, -1]))  # 实例3
