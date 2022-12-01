# -*- coding: utf-8 -*-
import copy


def homo_list_length(list_bench, list_addon):
    list_bench_temp = copy.deepcopy(list_bench)
    list_addon_temp = copy.deepcopy(list_addon)
    list_bench_len = len(list_bench)
    list_addon_len = len(list_addon)
    if list_bench_len < list_addon_len:
        for index in range(list_bench_len, list_addon_len):
            list_bench_temp.append(0)
    elif list_addon_len < list_bench_len:
        for index in range(list_addon_len, list_bench_len):
            list_addon_temp.append(0)
    return list_bench_temp, list_addon_temp


def compare_list_element(list_a, list_b):
    result = []
    list_ta, list_tb = homo_list_length(list_a, list_b)
    for index in range(0, len(list_ta)):
        element_a, element_b = list_ta[index], list_tb[index]
        if element_a < element_b:
            result.append(0)
        else:
            result.append(1)
    return result


def transfer_element_type(element, expect_type):
    """
    实现对元素进行指定类型的转换
    :param element:
    :param expect_type:
    :return:
    """
    #  ToDo：此处类型可能不完善，还需要补充，目前只考虑到了int, float, string
    #  ToDo：如果类型之间无法转换，应该用Traceback来锁定错误及提示错误内容
    if expect_type == float:
        return float(element)
    elif expect_type == int:
        return int(element)
    else:
        return str(element)


def homo_type_list(list_sample, index):
    """
    实现指定index的元素类型为全部元素类型
    :param list_sample:
    :param index:
    :return:
    """
    result = []
    if index >= len(list_sample):
        index = 0  # 防止越界
    index_element_type = type(list_sample[index])
    for element in list_sample:
        result.append(transfer_element_type(element, index_element_type))
    return result

