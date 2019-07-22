#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 3:58 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : lru_cache.py
# @Software: IntelliJ IDEA

class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

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


    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
            if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
                self.pop_front()					#删除头部

lru = LRUCache(3)
lru.set("a", "aaa")
lru.set("a", "bbb")
lru.set("a", "ccc")
# lru.set("d", "ddd")
# lru.get("a")
lru.get_cur_linkedlist()
