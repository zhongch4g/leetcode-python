#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 11:04 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 84. Largest Rectangle in Histogram.py
# @Software: IntelliJ IDEA


# 单调栈
class Solution:
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0

        stack = []
        maxr = 0
        for i in range(len(heights) + 1):
            curt = -1 if i == len(heights) else heights[i]
            while stack and curt <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                maxr = max(maxr, h * w)
            stack.append(i)
        return maxr


# 开辟两个数组，记录当前点，到左边或右边第一个比它小的高度的距离
class Solution1:
    def largestRectangleArea(self, heights) -> int:
        length = len(heights)
        if length == 0:
            return 0
        left = [1] * length
        right = [1] * length

        #left[i] to indicate how many bars to the left (including the bar at index i) are equal or higher than bar[i]
        for i in range(1, length):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j

        for p in range(length - 2, -1, -1):
            q = p + 1
            while q <= length - 1 and heights[q] >= heights[p]:
                q += right[q]
            right[p] = q - p

        m = -1
        for i in range(length):
            m = max(m, (left[i] + right[i] - 1) * heights[i])
        return m


solution = Solution()
solution.largestRectangleArea([2,1,5,6,2,3])