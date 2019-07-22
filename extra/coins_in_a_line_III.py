#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 11:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : coins_in_a_line_III.py
# @Software: IntelliJ IDEA


class Solution:
    def coins_in_a_line_III(self, nums):

        dp = [[-1]*len(nums) for i in range(len(nums))]
        total = 0
        # Initialize
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            total += nums[i]
            if i + 1 < len(nums):
                dp[i][i+1] = max(nums[i], nums[i+1])
        self.search(nums, 0, len(nums) - 1, dp)
        print(dp)
        return dp[0][len(nums)-1] > (total/2)

    def search(self, nums, i, j, dp):

        if i <= j and dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = max(
            min(self.search(nums, i+2, j, dp), self.search(nums, i+1, j-1, dp)) + nums[i],
            min(self.search(nums, i+1, j-1, dp), self.search(nums, i, j-2, dp)) + nums[j],
        )
        return dp[i][j]



"""
two people pick coin from two side, and each time can only pick one coin.
Q: can first people win or not

"""
solution = Solution()
res = solution.coins_in_a_line_III([3,2,2])
print(res)