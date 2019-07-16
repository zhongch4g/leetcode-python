#-*-coding:utf-8 -*-
"""
    53. Maximum Subarray
    Directed by user zhongch4g
    current system date 2019/7/15
"""
import sys


class Solution(object):
    def maxSubArray(self, nums):
        prefix_sum = 0
        min_sum, max_sum = 0, -sys.maxsize - 1
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        print(max_sum)


    """
    divide conquer version
    """
    def maxSubArray2(self, nums):
        if not nums:
            return 0
        max_subarray = self.max_sub_array(nums, 0, len(nums) - 1)
        print(max_subarray)
        return max_subarray

    def max_sub_array(self, nums, i, j):
        if i == j:
            return nums[i]
        else:
            mid = (i + j) // 2
            left_subarray  = self.max_sub_array(nums, i, mid)
            right_subarray = self.max_sub_array(nums, mid + 1, j)

            cross_subarray = self.cross_subarray(nums, i, mid, j)

            if left_subarray >= right_subarray and left_subarray >= cross_subarray:
                return left_subarray
            elif right_subarray >= left_subarray and right_subarray >= cross_subarray:
                return right_subarray
            else:
                return cross_subarray


    def cross_subarray(self, nums, i, mid, j):
        left_max = -sys.maxsize - 1
        left = 0
        left_index = 0
        for l in range(mid, i - 1, -1):
            left += nums[l]
            if left > left_max:
                left_max = left
                left_index = l

        right_max = -sys.maxsize - 1
        right = 0
        right_index = 0
        for l in range(mid + 1, j + 1):
            right += nums[l]
            if right > right_max:
                right_max = right
                right_index = l

        return left_max + right_max




solution = Solution()
solution.maxSubArray2([-1,-1,-2,-2])

