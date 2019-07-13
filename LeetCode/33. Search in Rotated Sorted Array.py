#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 12:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 33. Search in Rotated Sorted Array.py
# @Software: IntelliJ IDEA


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
res = solution.search(nums, target)
print(res)