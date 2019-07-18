#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 5:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 72. Edit Distance.py
# @Software: IntelliJ IDEA


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for i in range(len(word1)+1)]

        # init
        for i in range(len(dp)):
            dp[i][0] += i
        for j in range(len(dp[0])):
            dp[0][j] += j
        print(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[len(word1)][len(word2)]


    def minDistance2(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for i in range(2)]

        for j in range(1, len(dp[0])):
            dp[0][j] = j
        print(dp)
        for i in range(1, len(word1) + 1):
            dp[i%2][0] = i
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i%2][j] = min(dp[(i - 1)%2][j - 1], dp[(i - 1)%2][j] + 1, dp[i%2][j - 1] + 1)
                else:
                    dp[i%2][j] = min(dp[(i - 1)%2][j - 1] + 1, dp[(i - 1)%2][j] + 1, dp[i%2][j - 1] + 1)
        return dp[len(word1)%2][len(word2)]



word1 = ""
word2 = "a"
solution = Solution()
res = solution.minDistance2(word1, word2)
print(res)