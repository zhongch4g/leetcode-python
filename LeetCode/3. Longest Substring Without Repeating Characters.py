#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 2:11 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 3. Longest Substring Without Repeating Characters.py
# @Software: IntelliJ IDEA


class Solution:
    def lengthOfLongestSubstring(self, s):
        i,j = 0, 0
        d = dict()
        length = 0
        while j < len(s):
            if s[j] in d:
                i = max(d[s[j]]+1, i)

            if j - i + 1 > length:
                length = j - i + 1
            d[s[j]] = j
            j += 1
        return length


solution = Solution()
res = solution.lengthOfLongestSubstring("tmmzuxt")
print(res)



