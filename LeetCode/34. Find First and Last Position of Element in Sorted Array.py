#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 5:41 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 34. Find First and Last Position of Element in Sorted Array.py
# @Software: IntelliJ IDEA


class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        i, j = -1, -1
        left, right = 0, len(nums) - 1

        # find the right
        while left + 1 < right:
            mid = (left + right) // 2
            # 如果碰到相同的会一直往右边靠 直到最后一个nums[mid] == target
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            j = right
        elif nums[left] == target:
            j = left

        left, right = 0, len(nums) - 1

        # find the left
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            i = left
        elif nums[right] == target:
            i = right

        if i == -1 and j == -1:
            return [-1, -1]

        return [i, j]


nums = [2,2]
target = 2
solution = Solution()
res = solution.searchRange(nums, target)
print(res)