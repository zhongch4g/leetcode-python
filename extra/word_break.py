#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 10:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_break.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    # Will Runtime error
    def wordBreak(self, s, wordDict):
        results = []
        self.dfs(s, [], results, wordDict)
        return results

    def dfs(self, s, substring, results, wordDict):
        if len(s) == 0:
            results.append(list((substring)))

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in wordDict:
                substring.append(prefix)
                self.dfs(s[i:], substring, results, wordDict)
                substring.pop()

solution = Solution()
results = solution.wordBreak("lintcode", ["de","ding","co","code","lint"])
print(results)