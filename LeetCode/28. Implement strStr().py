#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 7:54 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 28. Implement strStr().py
# @Software: IntelliJ IDEA


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        # Memory Limit Exceeded
        # dp = [(len(haystack) + 1) * [0] for i in range(len(needle)+1)]

        # Time Limit Exceeded
        # rolling array
        dp = [(len(haystack) + 1) * [0] for i in range(2)]
        for i in range(1, len(needle)+1):
            for j in range(1, len(haystack) + 1):
                if needle[i-1] == haystack[j-1]:
                    dp[i%2][j] = dp[(i - 1)%2][j - 1] + 1
                if dp[i%2][j] == len(needle):
                    return j - len(needle)
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): # early termination
            return -1
        if not needle:
            return 0

        i = j = 0
        while j < len(needle) and i < len(haystack):
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
                continue
            i += 1
            j += 1
        return i - j if j == len(needle) else -1

    def strStr3(self, haystack: str, needle: str) -> int:

        if needle == '':
            return 0

        haystackLength = len(haystack)
        needleLength = len(needle)

        for i in range(haystackLength - needleLength + 1):
            flag = False
            if haystack[i] == needle[0]:
                flag = True
                j = 1
                while(j < needleLength):
                    if haystack[i + j] != needle[j]:
                        flag = False
                        break
                    j += 1
            if flag == True:
                return i

        return -1

solution = Solution()
res = solution.strStr3(haystack = "babadbac", needle = "bad")
print(res)