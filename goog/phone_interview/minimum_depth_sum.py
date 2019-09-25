#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 3:01 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : minimum_depth_sum.py
# @Software: IntelliJ IDEA

"""
给一堆球的高度，所有球以速度1m/s同时下降，着地后会1m/s往上弹（一直无限的弹上去）。
求什么时间所有球的高度和最小。

求 x 使得 f(x) = |x - x1| + |x - x2| + ... + |x - xn|
当 n = 2k + 1 时， x属于 [xk, xk + 1]
当 n = 2k 时， x属于 xk + 1
"""
class Solution:
    def minimum_depth_sum(self, depth):
        if not depth:
            return -1
        length = len(depth)
        if length & 1:
            return self.find_median(depth, length // 2 + 1)
        else:
            return [self.find_median(depth, length // 2), self.find_median(depth, length // 2 + 1)]


    def find_median(self, depth, k):
        m, n = 0, len(depth) - 1
        index = self.partition(depth, m, n)
        while index != k - 1:
            if index > k - 1:
                index = self.partition(depth, m, index - 1)
            if index < k - 1:
                index = self.partition(depth, index + 1, n)
        return depth[index]


    def partition(self, depth, left, right):
        pivot = depth[right]
        cur = left
        for i in range(left, right):
            if depth[i] <= pivot:
                depth[i], depth[cur] = depth[cur], depth[i]
                cur += 1
        depth[right], depth[cur] = depth[cur], depth[right]
        return cur


solution = Solution()
res = solution.minimum_depth_sum([2, 1, 3])
print(res)

