# -*- coding:utf-8 -*-

from typing import Optional



class ArrayQueue:
    '''
    数组实现队列
    '''

    def __init__(self, capacity: int):
        self._array = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                print('队列已经满')
                return False
            else:
                # for i in range(0, self._tail - self._head):
                #     self._array[i] = self._array[i + self._head]
                # self._tail = self._tail - self._head
                # self._head = 0

                self._array[0: self._tail - self._head] = self._array[self._head: self._tail]
                self._tail -= self._head
                self._head = 0

        self._array.insert(self._tail, value)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            value = self._array[self._head]
            self._head += 1
            return value
        else:
            return None

    def __repr__(self) -> str:
        return " <- ".join([item for item in self._array[self._head: self._tail]])

if __name__ == '__main__':
    queue = ArrayQueue(5)
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    queue.enqueue('5')
    print(queue)
    print(queue.dequeue())
    print(queue)
