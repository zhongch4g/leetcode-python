#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 11:13 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 49. Group Anagrams.py
# @Software: IntelliJ IDEA


class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        results = {}
        for i in strs:
            k = tuple(sorted(i))
            results.setdefault(k, [])
            results[k].append(i)
        print(list(results.values()))



solution = Solution()
solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])