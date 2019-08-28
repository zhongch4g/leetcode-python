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


class Solution2:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        self.father = {i: i for i in nums}
        self.size = {i: 1 for i in nums}

        for num in nums:

            if num - 1 in nums:
                self.union(num, num - 1)
            if num + 1 in nums:
                self.union(num, num + 1)
        return max(self.size.values())

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]