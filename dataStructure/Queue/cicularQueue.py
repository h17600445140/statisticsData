# -*- coding:utf-8 -*-
from typing import Optional
from itertools import chain



class CircularQueue:

    def __init__(self, capacity):
        self._array = []
        self._capacity = capacity + 1
        self._tail = 0
        self._head = 0

    def enqueue(self, value: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False

        self._array.append(value)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            value = self._array[self._head]
            self._head = (self._head + 1) % self._capacity
            return value

    def __repr__(self):
        if self._tail >= self._head:
            return " <- ".join([item for item in self._array[self._head: self._tail]])
        else:
            return " <- ".join([item for item in chain(self._array[self._head:], self._array[:self._tail])])

if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(10):
        q.enqueue(str(i))

    print(q)
    # print(q.dequeue())
    # q.dequeue()
    # q.enqueue(str(5))
    # print(q)