#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 4:12 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 148. Sort List.py
# @Software: IntelliJ IDEA


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        length = 0
        trav = head
        while trav:
            length += 1
            trav = trav.next

        # divide & conquer
        h = self.sort_linked_list(head, length)
        while h:
            print(h.val)
            h = h.next


    def sort_linked_list(self, root, length):
        if length <= 1 or not root or not root.next:
            return root

        first = root
        second = root
        mid = length // 2
        while mid > 0:
            temp = second
            second = second.next
            if mid == 1:
                temp.next = None
            mid -= 1

        l = self.sort_linked_list(first, length // 2)
        r = self.sort_linked_list(second, length - length // 2)

        dummy = ListNode(0)
        trav = dummy
        while l and r:
            if l.val > r.val:
                trav.next = r
                r = r.next
            else:
                trav.next = l
                l = l.next
            trav = trav.next
        if l:
            trav.next = l
        if r:
            trav.next = r
        return dummy.next


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
solution = Solution()
solution.sortList(node1)