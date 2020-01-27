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

import sys
class Solution2:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        counter = {c: 0 for c in s}
        maxlen = - sys.maxsize - 1
        j = 0
        for i in range(length):
            while j < length and counter[s[j]] == 0:
                maxlen = max(maxlen, j - i + 1)
                counter[s[j]] += 1
                j += 1
            counter[s[i]] -= 1
        return maxlen if maxlen != - sys.maxsize - 1 else 0




