#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 7:14 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 76. Minimum Window Substring.py
# @Software: IntelliJ IDEA


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        cntS = [0 for i in range(256)]
        cntT = [0 for j in range(256)]

        K = 0
        for c in t:
            cntT[ord(c)] += 1
            if cntT[ord(c)] == 1:
                K += 1
        C = 0
        r = 0
        ansl, ansr = -1, -1
        for l in range(len(s)):

            while r < len(s) and C < K:
                cntS[ord(s[r])] += 1
                if cntS[ord(s[r])] == cntT[ord(s[r])]:
                    C += 1
                r += 1

            if C == K:
                if ansl == -1 or r - l < ansr - ansl:
                    ansr = r
                    ansl = l

            cntS[ord(s[l])] -= 1
            if cntS[ord(s[l])] == cntT[ord(s[l])] - 1:
                C -= 1
        return s[ansl: ansr]


S = "ADOBECODEBANNC"
T = "ABC"
solution = Solution()
res = solution.minWindow(S, T)
print(res)