#-*-coding:utf-8 -*-
"""
    21. Merge Two Sorted Lists
    Directed by user zhongch4g
    current system date 2017/5/3
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode(0)
        relist = newList
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                newList.next = l2
                l2 = l2.next
                newList = newList.next
            else:
                newList.next = l1
                l1 = l1.next
                newList = newList.next
        if not l1:
            newList.next = l2
            return relist.next
        if not l2:
            newList.next = l1
            return relist.next