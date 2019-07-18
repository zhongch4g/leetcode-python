#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 7:14 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 76. Minimum Window Substring.py
# @Software: IntelliJ IDEA

import sys
import collections

class Solution:
    # Follow-up: allow for at most 1 character of difference
    def minWindow(self, s, t):
        counts = collections.Counter(t)
        numToMatch = len(counts)
        result = ''
        n = len(s)
        left = right = 0
        minLen = float('inf')
        while right < n:
            counts[s[right]] -= 1
            if counts[s[right]] == 0:
                numToMatch -= 1
            while numToMatch <= 1:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    result = s[left : right + 1]
                counts[s[left]] += 1
                if counts[s[left]] > 0:
                    numToMatch += 1
                left += 1
            right += 1
        return result

    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        targetSet = {}
        for c in t:
            targetSet[c] = targetSet.get(c, 0) + 1
        targetNumber = len(targetSet)

        minLen = len(s) + 1
        result = ''
        i = 0
        for j in range(len(s)):
            if s[j] in targetSet:
                targetSet[s[j]] -= 1
                if targetSet[s[j]] == 0:
                    targetNumber -= 1

            while targetNumber == 0:
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    result = s[i : j + 1]
                if s[i] in targetSet:
                    targetSet[s[i]] += 1
                    if targetSet[s[i]] > 0:
                        targetNumber += 1
                i += 1

        return result


S = "ADOBECODEBANNC"
T = "ABC"
solution = Solution()
res = solution.minWindow2(S, T)
print(res)