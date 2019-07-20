#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 10:44 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 128. Longest Consecutive Sequence.py
# @Software: IntelliJ IDEA


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = set(nums)
        longest = 0
        for i in nums:
            if i - 1 not in h:
                curr = 1
                curr_num = i
                while curr_num + 1 in h:
                    curr += 1
                    curr_num += 1
                longest = max(longest, curr_num)
        return longest