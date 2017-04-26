#-*-coding:utf-8 -*-
"""
    268. Missing Number
    Directed by user zhongch4g
    current system date 2017/4/26
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # algorithm should run in linear runtime complexity

        # Time Limit Exceeded
        # sorted_nums = sorted(nums)
        # for i in range(len(sorted_nums) + 1):
        #     if i in sorted_nums:
        #         continue
        #     else:
        #         return i

        n = len(nums)
        return n * (n + 1) / 2  - sum(nums)
instance = Solution()
print instance.missingNumber([0, 1, 3])
# print bin(4), bin(3)
