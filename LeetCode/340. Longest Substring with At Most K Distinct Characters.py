#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 10:50 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 340. Longest Substring with At Most K Distinct Characters.py
# @Software: IntelliJ IDEA


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:


        counter = [0 for i in range(256)]
        C = 0
        r = 0
        maxlen = -1
        for l in range(len(s)):
            while r < len(s) and C <= k:
                counter[ord(s[r])] += 1
                if counter[ord(s[r])] == 1:
                    C += 1
                # important
                if C <= k:
                    maxlen = max(maxlen, r - l + 1)
                r += 1


            counter[ord(s[l])] -= 1
            if counter[ord(s[l])] == 0:
                C -= 1

        return maxlen if maxlen != -1 else 0
