#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 10:12 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 142. Linked List Cycle II.py
# @Software: IntelliJ IDEA


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head: ListNode):
        h = set()
        trav = head
        while trav:
            if trav not in h:
                h.add(trav)
            else:
                return trav
            trav = trav.next

        return None


    def detectCycle2(self, head: ListNode):
        if not head or not head.next:
            return None
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next
            if not fast or not fast.next:
                return None

            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None




node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
solution = Solution()
res = solution.detectCycle2(node1)
print(res.val)