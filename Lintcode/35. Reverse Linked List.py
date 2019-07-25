#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 2:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 35. Reverse Linked List.py
# @Software: IntelliJ IDEA


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head:
            return head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


    def reverse2(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next