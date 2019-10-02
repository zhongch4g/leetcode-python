#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 8:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 410. Split Array Largest Sum.py
# @Software: IntelliJ IDEA


# 划分型动态规划
import sys
class Solution:
    def splitArray(self, nums, m: int) -> int:
        if not nums:
            return 0

        n = len(nums)

        if m > n:
            m = n

        # initial
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[0][i] = sys.maxsize

        # presum
        presum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]
        # print(presum)

        for i in range(1, m + 1):
            dp[i][0] = 0
            for j in range(1, n + 1):
                dp[i][j] = sys.maxsize
                s = 0
                for k in range(j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], presum[j] - presum[k]))
                    # for k in range(j, -1, -1):
                    #     dp[i][j] = min(dp[i][j], max(dp[i - 1][k], s))
                    #     if k > 0:
                    #         s += nums[k - 1]
        return dp[m][n]


# greedy
"""
如果我们可以找到一种分割方法来确保最大的子数组和不会超过一个值x，
那么我们也可以找到一种分割方法来确保最大的子数组和不会超过任何大于x的值y。
"""
import sys
class Solution:
    def splitArray(self, nums, m: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left + 1 < right:
            # print(left, right, (left + right) >> 1)
            mid = (left + right) >> 1
            if self.is_valid_partition(nums, mid, m):
                # if mid can let k(k <= m) parts sum smaller than mid, means mid is too large
                right = mid
            else:
                left = mid
        # must be [False, False, ..., False, True, ..., True ]
        if self.is_valid_partition(nums, left, m):
            return left
        else:
            return right


    def is_valid_partition(self, nums, n, m):
        cnt = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > n:
                cnt += 1
                cur_sum = num

        if cnt <= m:
            return True
        else:
            return False

