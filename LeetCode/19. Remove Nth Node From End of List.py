#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 11:57 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 19. Remove Nth Node From End of List.py
# @Software: IntelliJ IDEA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # corner case
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        length = 0
        # if length > len(ListNode)
        cur = dummy
        while cur.next is not None:
            cur = cur.next
            length += 1
        if n > length:
            return dummy.next

        idx1 = dummy
        idx2 = dummy

        length = 0
        for i in range(n):
            idx2 = idx2.next

        while idx2.next is not None:
            idx1 = idx1.next
            idx2 = idx2.next
            length += 1

        idx1.next = idx1.next.next
        return dummy.next


node = ListNode(1)
n = 1
solution = Solution()
res = solution.removeNthFromEnd(node, n)
print(res)