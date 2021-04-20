# -*- coding:utf-8 -*-



class Node(object):
    ''' 定义一个节点 '''

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        self.__next_node = node



class SinglyLinkedList(object):

    def __init__(self):
        self.__head = None

    def create_node(self, value, next_node=None) -> Node:
        '''
        创建一个节点
        :param value:
        :return:
        '''
        return Node(value, next_node)

    def insert_node_to_head(self, node: Node) -> None:
        '''
        插入节点到头节点前
        :param node:
        :return:
        '''
        if self.__head != None:
            node.next_node = self.__head
            self.__head = node
        else:
            self.__head = node

    def insert_to_head(self, value) -> None:
        '''
        在链表头部插入一个存储值为value数值的node节点
        :param value:node value
        :return:
        '''
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_node_after(self, node: Node, value) -> None:
        '''
        在指定节点之后插入值为value的节点
        :param node:
        :param value:
        :return:
        '''
        if node == None:
            return

        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next = new_node

    def insert_node_before(self, node: Node, value) -> None:
        '''
        在指定节点之前插入值为value的节点
        :param node:
        :param value:
        :return:
        '''
        if node == None or self.__head == None:
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pre = self.__head
        not_found = False
        while pre.next_node != node:
            if pre.next_node is None:
                not_found = True
                break
            else:
                pre = pre.next_node
        if  not not_found:
            pre.next_node = new_node
            new_node.next_node = node

    def delete_by_value(self, value) -> None:
        '''
        删除链表中从头开始第一个value值
        :param value:
        :return:
        '''
        if self.__head == None:
            return

        if self.__head.data == value:
            self.__head = self.__head.next_node
            return

        position = self.__head
        if position.next_node == None:
            print('没有找到相应的值')
            return
        while position.next_node.data != value:
            position = position.next_node
            if position.next_node == None:
                print('没有找到相应的值')
                return
        position.next_node = position.next_node.next_node

    def delete_by_values(self, value) -> None:
        '''
        删除链表中所有的value值
        :param value:
        :return:
        '''
        if self.__head == None:
            return

        while self.__head.data == value:
            self.__head = self.__head.next_node

        position = self.__head
        while position.next_node != None:
            if position.next_node.data != value:
                position = position.next_node
                continue
            if position.next_node.data == value:
                position.next_node = position.next_node.next_node

    def delete_by_node(self, node: Node) -> None:
        '''
        在链表中删除指定节点
        :param node:
        :return:
        '''
        if self.__head == None:
            return

        if self.__head == node:
            self.__head = self.__head.next_node

        position = self.__head
        flag = False
        while position.next_node != node:
            if position.next_node == None:
                flag = True
                break
            else:
                position = position.next_node
        if not flag:
            position.next_node = node.next_node

    def delete_last_n_node(self, n) -> None:
        '''
        删除链表倒数第几个节点
        :param n:
        :return:
        '''
        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            tmp = slow
            fast = fast.next_node
            slow = slow.next_node

        tmp.next_node = slow.next_node

    def find_node_by_value(self, value) -> Node:
        '''
        根据value查找离头节点最近的一个节点
        :param value:
        :return:
        '''
        node = self.__head
        while (node.data) != None and (node.data != value):
            node = node.next_node
        return node

    def printSinglyLinkedList(self) -> None:
        '''
        打印链表
        :return:
        '''
        position = self.__head
        if position == None:
            print("当前单链表还没有任何数据")
            return
        while position.next_node != None:
            print(str(position.data) + ' -> ',end="")
            position = position.next_node
        print(position.data)

    def find_mid_node(self)  -> None:
        '''
        查找链表中间节点
        :return:
        '''
        fast = self.__head
        slow = self.__head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow

    def has_ring(self) -> bool:
        '''
        判断链表是否有环
        :return:
        '''
        fast = self.__head
        slow = self.__head

        while (fast is not None) and (fast.next_node is not None):
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True

        return False

    def reversed_self(self) -> None:
        '''
        翻转链表本身
        :return:
        '''
        if self.__head == None or self.__head.next_node == None:
            return

        pre = self.__head
        node = self.__head.next_node
        while node != None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self.__head.next_node = None
        self.__head = pre

    def __reversed_with_two_node(self, pre: Node, node: Node) -> (Node, Node):
        '''
        翻转相邻两个节点
        :param pre:
        :param node:
        :return:
        '''
        tmp = node.next_node
        node.next_node = pre
        pre = node
        node = tmp
        return pre, node




if __name__ == '__main__':

    linkedList = SinglyLinkedList()

    # 1
    # linkedList.insert_to_head('1')
    # linkedList.insert_to_head('2')
    # linkedList.insert_to_head('3')
    # linkedList.insert_to_head('4')
    # linkedList.insert_to_head('5')
    # linkedList.insert_to_head('1')
    # linkedList.insert_to_head('2')
    # linkedList.insert_to_head('3')
    # linkedList.insert_to_head('3')
    # linkedList.insert_to_head('3')
    # linkedList.delete_by_values

    # 2
    # B = linkedList.create_node('B')
    # C = linkedList.create_node('C',next_node=B)
    # A = linkedList.create_node('A',next_node=C)
    # D = linkedList.create_node('D')
    # E = linkedList.create_node('E')
    # linkedList.insert_node_to_head(A)
    # linkedList.insert_node_to_head(B)
    # linkedList.insert_node_to_head(C)
    # linkedList.insert_node_to_head(D)
    # linkedList.insert_node_to_head(E)
    # print(linkedList.has_ring())

    # 3
    # linkedList.insert_to_head('1')
    # linkedList.insert_to_head('2')
    # linkedList.insert_to_head('3')
    # node = linkedList.find_by_value('2')
    # print(node.data)

    # 4
    # linkedList.insert_to_head('1')
    # linkedList.insert_to_head('2')
    # linkedList.insert_to_head('3')
    # linkedList.reversed_self()


    linkedList.printSinglyLinkedList()



