#-*-coding:utf-8 -*-
"""
    # @File    : 674. Longest Continuous Increasing Subsequence.py
    # @Author  : zhongch4g
    # @Time    : 2017/11/3 11:26
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N)
        # if len(nums) == 0 or len(nums) == 1:
        #     return len(nums)
        #
        # cnt, tmp = 1, 1
        # for i in range(1, len(nums)):
        #     # 当前索引为最后一个
        #     if i == (len(nums) - 1) and nums[i] > nums[i - 1]:
        #         tmp += 1
        #         if tmp > cnt:
        #             cnt = tmp
        #         return cnt
        #     elif i == (len(nums) - 1) and nums[i] <= nums[i - 1]:
        #         return cnt
        #     if i < (len(nums) - 1) and nums[i] > nums[i - 1]:
        #         tmp += 1
        #         cnt = tmp
        #     if tmp >= cnt and nums[i] <= nums[i - 1]:
        #         cnt = tmp
        #         tmp = 1

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        cnt, tmp = 1, 1
        for i in range(1, len(nums)):
            # 首先判断边界情况（第一个和最后一个）
            if nums[i] > nums[i - 1]:
                tmp += 1
            if nums[i] <= nums[i - 1] or i == len(nums) - 1:
                if tmp > cnt:
                    cnt = tmp
                tmp = 1
        return cnt


instance = Solution()
print(instance.findLengthOfLCIS([1,3,5,7,5,3,4,5,6,7]))


