#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 8:16 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 647. Find All Anagrams in a String.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        lens = len(s)
        lenp = len(p)
        st = [0] * 30
        for c in p:
            st[ord(c) - ord('a')] += 1
        res = []
        start, end, matched = 0, 0, 0
        while end < lens:
            if st[ord(s[end]) - ord('a')] >= 1:
                matched += 1
            st[ord(s[end]) - ord('a')] -= 1

            if matched == lenp:
                res.append(start)

            end += 1

            if end - start == len(p):
                if st[ord(s[start]) - ord('a')] >= 0:
                    matched -= 1
                st[ord(s[start]) - ord('a')] += 1

                start += 1
        return res


s = "cbaebabacd"
p = "abc"
solution = Solution()
res = solution.findAnagrams(s, p)
print(res)