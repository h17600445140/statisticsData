# -*- coding: utf-8 -*-
# Author: HuangChao
# 自定义数据


class Array:

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, position: int) -> object:
        try:
            return self._data[position]
        except IndexError:
            raise None

    def delete(self, position: int) -> bool:
        try:
            self._data.pop(position)
            return True
        except IndexError:
            return False

    def insert(self, position: int, value: object) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(position, value)
            return True

    def print_array(self):
        for i in self._data:
            print(i, end="")

if __name__ == '__main__':
    myArray = Array(10)
    myArray.insert(0,1)
    myArray.insert(1,2)
    myArray.print_array()

    print()

    myArray.delete(1)
    myArray.insert(2,3)
    myArray.insert(3,4)
    myArray.insert(4,5)
    myArray.print_array()

    print()

    print(myArray[1])

    print(myArray.find(1))

    myArray[3] = 10
    myArray.print_array()

    print()

    for i in myArray:
        print(i, end=" ")




