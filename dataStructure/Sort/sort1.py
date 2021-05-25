# -*- coding:utf-8 -*-
from typing import List


def bubble_sort(list: List[int]):
    '''
    冒泡排序
    :param list:
    :return:
    '''
    listLength = len(list)

    if listLength <= 1 :
        return list

    for i in range(listLength):
        swap = False
        for j in range(listLength-1-i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j], a[j+1] = a[j+1], temp
                swap = True
        if not swap:
            break

    return list


def insertion_sort(list: List[int]):
    '''
    插入排序
    :param list:
    :return:
    '''
    listLength = len(list)

    if listLength <= 1:
        return list

    for i in range(1, listLength):
        value = list[i]
        j = i -1
        while j>=0 and list[j] > value:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = value

    return list


def selection_sort(list: List[int]):
    '''
    选择排序
    :param list:
    :return:
    '''
    listLength = len(list)

    if listLength <= 1:
        return list

    for i in range(listLength):
        min_index = i
        min_value = list[i]
        for j in range(i, listLength):
            if list[j] < min_value:
                min_index = j
                min_value = list[j]
  
        # list[min_index] = list[i]
        # list[i] = min_value
        list[min_index], list[i] = list[i], list[min_index]

    return list


if __name__ == '__main__':
    a = [5,4,8,6,1,2]

    # print(bubble_sort(a))
    # print(insertion_sort(a))
    print(selection_sort(a))