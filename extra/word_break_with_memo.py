#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 11:18 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_break_with_memo.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    # Will Runtime error
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    # return all the combination of s
    # @ must return value when using memoization
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []

        partitions = []
        if s in wordDict:
            partitions.append(s)

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordDict:
                partition_sub = self.dfs(s[i:], wordDict, memo)
                for partition in partition_sub:
                    partitions.append(prefix + " " + partition)
        memo[s] = partitions
        return partitions

solution = Solution()
results = solution.wordBreak("lintcode", ["de","ding","co","code","lint"])
print(results)