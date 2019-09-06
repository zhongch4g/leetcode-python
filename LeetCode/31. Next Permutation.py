#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 9:49 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 31. Next Permutation.py
# @Software: IntelliJ IDEA


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # step 1: find the first descending number from the back to the front
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # step 2: find the first number that bigger than nums[i] from the back to the front
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # step3: reverse from i + 1 to the end
        nums[i+1:] = nums[i+1:][::-1]


    def nextPermutation2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        i = len(nums) - 1
        # find the first increasing number
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # reverse from increasing number to the end
        nums[i:] = reversed(nums[i:])
        print(nums, i - 1, i)
        # from reversed numbers find the first number that bigger than increasing number
        if i > 0:
            pivot = i - 1
            while i < len(nums) and nums[i] <= nums[pivot]:
                i += 1
            nums[pivot], nums[i] = nums[i], nums[pivot]
        return nums