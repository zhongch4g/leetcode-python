#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 5:53 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 138. Copy List with Random Pointer.py
# @Software: IntelliJ IDEA


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        reflect = {}
        nhead = Node(head.val, None, None)
        p = head
        reflect[head] = nhead
        q = nhead
        while p:
            q.random = p.random
            if p.next:
                q.next = Node(p.next.val, None, None)
                reflect[p.next] = q.next
            else:
                q.next = None

            p = p.next
            q = q.next

        p = nhead
        while p:
            if p.random:
                p.random = reflect[p.random]
            p = p.next
        return nhead