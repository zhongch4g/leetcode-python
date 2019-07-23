#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 1:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 627. Longest Palindrome.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def __init__(self):
        self.length = 0

    def longestPalindrome(self, s):
        if not s:
            return 0
        s = sorted(list(s))
        self.search(s, "", set())
        return self.length

    def search(self, s, curr, visited):
        if len(curr) > len(s):
            return

        if self.is_palindrome(curr) and len(curr) > self.length:
            self.length = len(curr)

        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1] and i - 1 not in visited:
                continue

            if i in visited:
                continue

            visited.add(i)
            self.search(s, curr + s[i], visited)
            visited.remove(i)


    def is_palindrome(self, s):
        return s == s[::-1]


    #############
    def longestPalindrome2(self, s):
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
        print(hash)
        remove = len(hash)
        if remove > 0:
            remove -= 1

        return len(s) - remove


solution = Solution()
solution.longestPalindrome2("kabccccdd")