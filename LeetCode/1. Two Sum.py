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
        # list_sorted = sorted(nums)
        # temp = 0
        # for i in range(len(list_sorted)):
        #     if list_sorted[i] > target:
        #         temp = i
        # if temp == 0:
        #     temp = len(list_sorted)
        # list1 = list(combinations(list_sorted[:temp], 2))
        # # print list1
        # for tuples in list1:
        #     if sum(tuples) == target:
        #         return [nums.index(tuples[0]), nums.index(tuples[1])]
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

instance = Solution()
print (instance.twoSum2([3, 2, 4], 6))