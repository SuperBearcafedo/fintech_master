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

