#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 3:06 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_k_sorted_arrays.py
# @Software: IntelliJ IDEA

import heapq
"""
@ heapq.heappush(heap, item):
Push the value item onto the heap, maintaining the heap invariant.

@ heapq.heappop(heap):
Pop and return the smallest item from the heap, maintaining the heap invariant. 
If the heap is empty, IndexError is raised.

@ heapq.heapify(x):
Transform list x into a heap, in-place, in linear time.
"""

# 创建自己的堆
class Heap:
    def __init__(self, init_data, arrays):
        self.key = lambda pos:arrays[pos.row][pos.col]
        if init_data:
            self.heap = [(self.key(i), i)for i in init_data]
            heapq.heapify(self.heap)
        else:
            self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return not self.heap


class Pos:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        heap = [(Pos(i, 0, arrays[i][0])) for i in range(len(arrays)) if arrays[i]]
        heapq.heapify(heap)
        result = []
        while heap:
            node = heapq.heappop(heap)
            result.append(node.value)
            if node.col + 1 < len(arrays[node.row]):
                heapq.heappush(heap, Pos(node.row, node.col + 1, arrays[node.row][node.col + 1]))
        print(result)





arrays = [
    [], []
    ]
arrays1 = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
solution = Solution()
solution.mergekSortedArrays(arrays1)




