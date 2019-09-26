#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 7:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 300. Longest Increasing Subsequence.py
# @Software: IntelliJ IDEA


class Solution:
    def lengthOfLIS(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0

        f = [0 for i in range(length)]
        longest = 0
        # print a path
        pi = [0 for i in range(length)]
        end_point = 0
        for i in range(length):
            f[i] = 1
            pi[i] = -1
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    f[i] = max(f[j] + 1, f[i])
                    if f[i] == f[j] + 1:
                        pi[i] = j
            longest = max(longest, f[i])
            if longest == f[i]:
                end_point = i
        res = [0 for i in range(longest)]
        for i in range(longest - 1, -1, -1):
            res[i] = nums[end_point]
            end_point = pi[end_point]
        for i in range(longest):
            print(res[i])
        return longest

