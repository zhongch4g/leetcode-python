#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 5:04 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 81. Search in Rotated Sorted Array II.py
# @Software: IntelliJ IDEA


class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


nums = [1,2,1]
target = 1
solution = Solution()
res = solution.search(nums, target)
print(res)