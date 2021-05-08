# -*- coding:utf-8 -*-

from typing import Optional



class Node:

    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next



class LinkedStack:

    def __init__(self):
        self._top = None

    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top

    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top.data
            self._top = self._top.next
            return value

    def __repr__(self):
        currentNode = self._top
        nums = []
        while currentNode:
            nums.append(str(currentNode.data))
            currentNode = currentNode.next
        print(nums)
        return '->'.join(nums)

if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)

