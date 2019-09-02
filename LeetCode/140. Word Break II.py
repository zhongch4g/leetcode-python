#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 12:22 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 140. Word Break II.py
# @Software: IntelliJ IDEA


class Solution:
    def wordBreak(self, s: str, wordDict):

        return self.search(s, wordDict, {})

    # return list that can represent s
    def search(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        partitions = []
        if s in wordDict:
            partitions.append(s)

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in wordDict:
                partition_sub = self.search(s[i:], wordDict, memo)
                for partition in partition_sub:
                    partitions.append(prefix + " " + partition)
        memo[s] = partitions
        return partitions


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog", "catsanddog"]
solution = Solution()
res = solution.wordBreak(s, wordDict)
print(res)