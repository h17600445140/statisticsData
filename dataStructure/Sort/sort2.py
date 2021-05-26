# -*- coding:utf-8 -*-
from typing import List
import random
import time

'''
    归并排序
'''

def merge_sort(list: List[int]):
    _merge_sort_between(list, 0, len(list)-1)

def _merge_sort_between(list: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(list, low, mid)
        _merge_sort_between(list, mid+1, high)
        _merge(list, low, mid, high)

def _merge(list: List[int], low: int, mid: int, high: int):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j<= high:
        if list[i] <= list[j]:
            tmp.append(list[i])
            i += 1
        else:
            tmp.append(list[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(list[start:end+1])
    list[low:high+1] = tmp


'''
    快速排序
'''

def quick_sort(list: List[int]):
    _quick_sort_between(list, 0, len(list)-1)

def _quick_sort_between(list: List[int], low: int, high: int):
    if low < high:
        k = random.randint(low, high)
        list[low], list[k] = list[k], list[low]

        m = _partition(list, low, high)
        _quick_sort_between(list, low, m-1)
        _quick_sort_between(list, m+1, high)

def _partition(list: List[int], low: int, high: int):
    pivot, j = list[low], low
    for i in range(low+1, high+1):
        if list[i] <= pivot:
            j += 1
            list[j], list[i] = list[i], list[j]
    list[low], list[j] = list[j], list[low]
    return j


if __name__ == '__main__':
    a = [3, 9, 6, 8, 0, 2]
    start_merge = time.time()
    print(start_merge)
    merge_sort(a)
    time.sleep(1)
    end_merge = time.time()
    print(end_merge)
    time_merge = end_merge - start_merge
    print(a)
    print(time_merge)

    b = [3, 9, 6, 8, 0, 2]
    start_quick = time.time()
    quick_sort(b)
    end_quick = time.time()
    time_quick = end_quick - start_quick
    print(b)
    print(time_quick)
