# -*- coding:utf-8 -*-


class LinkedListNode(object):

    def __init__(self, key, value, pre_node=None, next_node=None):
        self.pre_node = pre_node
        self.next_node = next_node
        self.key = key
        self.value = value



class LRUCache(object):
    '''
    LRU缓存淘汰算法
        内置函数：get，put
        原理：双向链表+哈希表
        效率：
            时间复杂度：查找O(1)，新增O(1)
    '''

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hkey = {}
        self._top = LinkedListNode(None, -1)
        self._tail = LinkedListNode(None, -1)
        self._top.next_node = self._tail
        self._tail.pre_node = self._top

    def get(self, key: int) -> int:
        if key in self._hkey.keys():
            cursor = self._hkey[key]
            # 跳出原位置
            cursor.pre_node.next_node = cursor.next_node
            cursor.next_node.pre_node = cursor.pre_node
            # 将最近用过的置于链表首部
            top_node = self._top.next_node
            self._top.next_node = cursor
            cursor.pre_node = self._top
            cursor.next_node = top_node
            top_node.pre_node = cursor
            return self._hkey[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._hkey.keys():
            cursor = self._hkey[key]
            cursor.value = value
            # 跳出原位置
            cursor.pre_node.next_node = cursor.next_node
            cursor.next_node.pre_node = cursor.pre_node
            # 将最近用过的置于链表首部
            top_node = self._top.next_node
            self._top.next_node = cursor
            cursor.pre_node = self._top
            cursor.next_node = top_node
            top_node.pre_node = cursor
        else:
            # 增加新节点置首部
            cursor = LinkedListNode(key, value)
            self._hkey[key] = cursor
            # 将最近用过的置于链表首部
            top_node = self._top.next_node
            self._top.next_node = cursor
            cursor.pre_node = self._top
            cursor.next_node = top_node
            top_node.pre_node = cursor
            # 超长去掉尾节点
            if len(self._hkey.keys()) > self._capacity:
                self._hkey.pop(self._tail.pre_node.key)
                self._tail.pre_node.pre_node.next_node = self._tail
                self._tail.pre_node = self._tail.pre_node.pre_node

    def __repr__(self):
        values = []
        cursor = self._top.next_node
        while cursor.next_node:
            values.append(str(cursor.value))
            cursor = cursor.next_node
        return '->'.join(values)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)

    print(cache.get(1))
    print(cache)

    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)

    print(cache.get(2))
    print(cache)

    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)

    print(cache.get(1))
    print(cache)

    print(cache.get(3))
    print(cache)

    print(cache.get(4))
    print(cache)

