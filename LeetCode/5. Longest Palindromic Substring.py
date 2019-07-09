#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 10:16 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 5. Longest Palindromic Substring.py
# @Software: IntelliJ IDEA


class Solution:
    # 最长回文子串
    def longestPalindrome(self, s):
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
                dp[i][i+1] = s[i] == s[i+1]
        for i in range(1, len(s)):
            dp[i][i-1] = s[i] == s[i-1]

        for i in range(len(dp)):
            print(dp[i])

        longest, start, end = 1, 0, 0
        # 规模
        for length in range(1, len(s)):
            for i in range(len(s)-length):
                j = i + length
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j] and longest < length + 1:
                    longest = length + 1
                    start = i
                    end = j
        return s[start:end+1]


    def longestPalindrome1(self, s):
        longest = ''
        for middle in range(len(s)):
            palin = self.palindrome(s, middle, middle)
            if len(palin) > len(longest):
                longest = palin
            palin = self.palindrome(s, middle, middle + 1)
            if len(palin) > len(longest):
                longest = palin
        return longest


    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


solution = Solution()
res = solution.longestPalindrome1("cbbd")
print(res)


