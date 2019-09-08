#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 10:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1186. Maximum Subarray Sum with One Deletion .py
# @Software: IntelliJ IDEA


import sys
class Solution1:
    def maximumSum(self, arr) -> int:
        pre = [None] * len(arr)
        pre[0] = arr[0]
        maxsum = arr[0]
        for i in range(1, len(arr)):
            pre[i] = max(arr[i], pre[i - 1] + arr[i])
            maxsum = max(maxsum, pre[i])

        back = [None] * len(arr)
        back[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            back[i] = max(arr[i], back[i + 1] + arr[i])

        for i in range(1, len(arr) - 1):
            maxsum = max(maxsum, pre[i - 1] + back[i + 1])
        return maxsum


class Solution:

    def maximumSum(self, arr) -> int:

        dp_left = self.calculate_dp(arr)
        dp_right = self.calculate_dp(arr[::-1])[::-1]
        print(dp_left)
        print(dp_right)

        # possible result that remove left end or right end element of that corresponding subarray
        result = max(*dp_right, *dp_left)
        # possible result that remove middle element of that corresponding subarray
        for i in range(1, len(arr) - 1):
            curr = dp_left[i - 1] + dp_right[i + 1]
            result = max(result, curr)

        return result


    # dp[i] stores the max sum among all the subarrays that end at i (include i)
    def calculate_dp(self, arr):
        dp = [0 for i in arr]
        sofar = 0
        for i in range(len(arr)):
            if sofar >= 0:
                dp[i] = arr[i] + sofar
            else:
                dp[i] = arr[i]
            sofar = dp[i]

        return dp

solution = Solution()
res = solution.maximumSum([1,-2,-2,3])
print(res)