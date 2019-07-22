#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 3:21 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_two_sorted_lists.py
# @Software: IntelliJ IDEA

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        index = dummy


        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                index.next = l1
                l1 = l1.next
                index = index.next
            else:
                index.next = l2
                l2 = l2.next
                index = index.next

        while l1 is not None:
            index.next = l1
            break

        while l2 is not None:
            index.next = l2
            break

        return dummy.next
