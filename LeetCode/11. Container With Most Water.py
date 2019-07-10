#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 9:06 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 11. Container With Most Water.py
# @Software: IntelliJ IDEA


class Solution:
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            cur_area = (right - left) * min_height
            if cur_area > max_area:
                max_area = cur_area

            if min_height == height[left]:
                left += 1
            else:
                right -= 1
        return max_area


solution = Solution()
res = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(res)