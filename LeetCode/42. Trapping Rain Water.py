#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 12:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 42. Trapping Rain Water.py
# @Software: IntelliJ IDEA


class Solution:
    def trap(self, height):
        left, right = 1, len(height) - 2
        left_max, right_max = 0, 0
        sum_trap = 0
        for i in range(1, len(height) - 1):
            # update left
            if height[left - 1] < height[right + 1]:
                left_max = max(left_max, height[left - 1])
                if left_max > height[left]:
                    sum_trap += (left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right + 1])
                if right_max > height[right]:
                    sum_trap += (right_max - height[right])
                right -= 1
        return sum_trap


height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
res = solution.trap(height)
print(res)