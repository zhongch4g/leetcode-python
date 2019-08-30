#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 12:17 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 159. Longest Substring with At Most Two Distinct Characters.py
# @Software: IntelliJ IDEA


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        counter = [0 for i in range(256)]
        r = 0
        C = 0
        maxlen = -1
        for l in range(len(s)):
            while r < len(s) and C <= 2:
                counter[ord(s[r])] += 1
                if counter[ord(s[r])] == 1:
                    C += 1
                if C <= 2 and r - l + 1 > maxlen:
                    maxlen = r - l + 1
                r += 1
            counter[ord(s[l])] -= 1
            if counter[ord(s[l])] == 0:
                C -= 1
        return maxlen if maxlen != -1 else 0
