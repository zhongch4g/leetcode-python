#-*-coding:utf-8 -*-
"""
    1. Two Sum
    Directed by user zhongch4g
    current system date 2017/5/16
"""
from itertools import combinations
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            # print i, num
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
            # print lookup
        return []


    # modify 07/08/2019
    def twoSum3(self, nums, target):
        res = dict()
        for idx, num in enumerate(nums):
            if (target - num) in res:
                return [res[target-num], idx]
            res[num] = idx



instance = Solution()
print (instance.twoSum2([3, 2, 4], 6))