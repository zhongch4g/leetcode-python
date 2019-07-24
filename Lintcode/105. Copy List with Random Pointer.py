#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 10:50 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 105. Copy List with Random Pointer.py
# @Software: IntelliJ IDEA


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        n_hash = {}
        n_head = RandomListNode(head.label)
        n_hash[head] = n_head
        p = head
        q = n_head
        while p:
            q.random = p.random
            if p.next:
                q.next = RandomListNode(p.next.label)
                n_hash[p.next] = q.next
            else:
                q.next = None

            p = p.next
            q = q.next

        p = n_head
        while p:
            if p.random is not None:
                p.random = n_hash[p.random]
            p = p.next
        return n_head
