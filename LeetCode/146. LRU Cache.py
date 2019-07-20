#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:29 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 146. LRU Cache.py
# @Software: IntelliJ IDEA


class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def get_cur_linkedlist(self):
        cur_head = self.dummy
        while cur_head:
            print(cur_head.value)
            cur_head = cur_head.next

    def push_back(self, node):
        # set curr tail node as prev node
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        # delete node
        prev.next = node.next
        if node.next is not None:
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.push_back(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # delete node and change the position
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
            if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
                self.pop_front()			#删除头部


        # 1.check the capacity
        # if capacity is not full
        # 2.add node to the first position
        # if capacity is full
        # 3.delete node then add node



        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(2))
obj.put(3, 3)
print(obj.get(1))
print(obj.get(3))
obj.get_cur_linkedlist()