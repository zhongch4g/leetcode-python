#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 11:38 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 24. Swap Nodes in Pairs.py
# @Software: IntelliJ IDEA


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

