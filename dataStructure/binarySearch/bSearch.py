# -*- coding:utf-8 -*-

from typing import List


'''
    传统二分查找
'''

def binarySearch1(list: List[int], target: int) -> int:
    '''
    二分查找
    :param list:
    :param target:
    :return:
    '''
    low, high = 0, len(list)-1
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

'''
    递归实现二分查找
'''

def binarySearch2(list: List[int], target: int) -> int:
    return binarySearch2_internally(list, target, 0, len(list)-1)

def binarySearch2_internally(list: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1

    mid = low + int((high - low) >> 2)
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binarySearch2_internally(list, target, mid+1, high)
    else:
        return binarySearch2_internally(list, target, low,  mid-1)


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9]

    print(binarySearch1(a, 4))
    print(binarySearch2(a, 4))

