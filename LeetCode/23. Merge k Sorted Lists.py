#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:45 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 23. Merge k Sorted Lists.py
# @Software: IntelliJ IDEA


import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeWrapper:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data.val < other.data.val

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        trav = dummy = ListNode(-1)
        # Initialization
        heap = []
        for head in lists:
            if head:
                self.heappushNode(heap, head)

        while heap:
            cur = heapq.heappop(heap).data
            trav.next = cur
            trav = trav.next

            if cur.next:
                self.heappushNode(heap, cur.next)

        return dummy.next


    def heappushNode(self, heap, node):
        heapq.heappush(heap, ListNodeWrapper(node))


    def mergeKLists2(self, lists):
        dummy = curr = ListNode(0)
        heap = [(n.val, i, n) for i,n in enumerate(lists) if n]
        heapq.heapify(heap)

        while len(heap) > 0:
            val, i, n = heap[0]
            if not n.next:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (n.next.val, i, n.next))

            curr.next = n
            curr = curr.next

        return dummy.next


list1 = ListNode(1)
node2 = ListNode(4)
list1.next = node2

list2 = ListNode(2)
node2 = ListNode(3)
list2.next = node2



solution = Solution()
res = solution.mergeKLists([list1, list2])
while res:
    print(res.val)
    res = res.next

