#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 9:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 139. Word Break.py
# @Software: IntelliJ IDEA


class Solution:
    def wordBreak(self, s, wordDict):
        if not s and not wordDict:
            return True
        if not s or not wordDict:
            return False
        return self.search(s, wordDict)

    def search(self, s, wordDict):
        if not s:
            return True

        for word in wordDict:
            if not s.startswith(word):
                continue
            if self.search(s[len(word):], wordDict):
                return True
        return False

    def wordBreak2(self, s, wordDict):
        if not s and not wordDict:
            return True
        if not s or not wordDict:
            return False
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return True
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            if self.dfs(s[i:], wordDict, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False


    def wordBreak3(self, s, wordDict):
        if not s and not wordDict:
            return True
        if not s or not wordDict:
            return False
        h = set()
        for word in wordDict:
            h.add(word)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in h:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]



s = "cars"
wordDict = ["car", "ca", "rs"]
solution = Solution()
res = solution.wordBreak3(s, wordDict)
print(res)