#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 11:02 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 2. Add Two Numbers.py
# @Software: IntelliJ IDEA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None or l2 is None:
            return 0

        res = ListNode(-1)
        cur = res
        remain = 0

        while l1 is not None and l2 is not None:
            num = (l1.val + l2.val + remain) % 10
            remain = (l1.val + l2.val + remain) // 10

            nn = ListNode(num)
            res.next = nn
            res = res.next

            l1 = l1.next
            l2 = l2.next


        while l1 is not None:
            num = (l1.val + remain) % 10
            remain = (l1.val + remain) // 10
            res.next = ListNode(num)
            res = res.next
            l1 = l1.next

        while l2 is not None:
            num = (l2.val + remain) % 10
            remain = (l2.val + remain) // 10
            res.next = ListNode(num)
            res = res.next
            l2 = l2.next

        if remain > 0:
            res.next = ListNode(remain)

        return cur.next


    def addTwoNumbers2(self, l1, l2):
        c1 = l1
        c2 = l2
        sentinel = ListNode(0)
        d = sentinel
        cur_sum = 0
        while c1 is not None or c2 is not None:
            cur_sum /= 10
            if c1 is not None:
                cur_sum += c1.val
                c1 = c1.next
            if c2 is not None:
                cur_sum += c2.val
                c2 = c2.next
            d.next = ListNode(cur_sum%10)
            d = d.next
        if cur_sum / 10 == 1:
            d.next = ListNode(1)
        return sentinel.next


"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
l = ListNode(-1)
l1 = ListNode(1)
# l.next = l1
# l1.next = ListNode(4)
# l1 = l1.next
# l1.next = ListNode(3)

lt = ListNode(9)
l2 = ListNode(9)
lt.next = l2
# l2.next = ListNode(6)
# l2 = l2.next
# l2.next = ListNode(4)

solution = Solution()
res = solution.addTwoNumbers2(l1, lt)
while res is not None:
    print(res.val)
    res = res.next