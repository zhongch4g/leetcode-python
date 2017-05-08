#-*-coding:utf-8 -*-
"""
    141. Linked List Cycle
    Directed by user zhongch4g
    current system date 2017/5/8
"""
# Definition for singly-linked list.
from collections import Set


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Can you solve it without using extra space?
        # Approach #1 (Hash Table)
        # nodeSeen = set()
        # while head is not None:
        #     if nodeSeen.__contains__(head):
        #         return True
        #     else:
        #         nodeSeen.add(head)
        #     head = head.next
        # return False
        # Approach #2 (Two Pointers)
        if head is not None or head.next is not None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True