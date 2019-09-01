#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 12:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 42. Trapping Rain Water.py
# @Software: IntelliJ IDEA


class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        leftmax = height[0]
        rightmax = height[-1]
        counter = 0
        left, right = 0, len(height) - 1
        while left <= right:
            if leftmax < rightmax:
                leftmax = max(leftmax, height[left])
                counter += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                counter += rightmax - height[right]
                right -= 1
        return counter

height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
res = solution.trap(height)
print(res)