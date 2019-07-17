#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 9:59 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 75. Sort Colors.py
# @Software: IntelliJ IDEA


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        index = 0
        while index <= j:
            if nums[index] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                i += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[j] = nums[j], nums[index]
                j -= 1

        print(nums)


solution = Solution()
solution.sortColors([2,0,2,1,2,0])