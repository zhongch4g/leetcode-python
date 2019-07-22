#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 4:10 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_pattern_II.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        return self.is_match(pattern, str, {}, set())

    def is_match(self, pattern, string, pat_wrd, used):

        # base case
        if not pattern:
            return not string

        letter = pattern[0]

        if letter in pat_wrd.keys():
            if not string.startswith(pat_wrd[letter]):
                return False
            return self.is_match(pattern[1:], string[len(pat_wrd[letter]):], pat_wrd, used)

        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue

            pat_wrd[letter] = word
            used.add(word)
            if self.is_match(pattern[1:], string[i + 1:], pat_wrd, used):
                return True
            del pat_wrd[letter]
            used.remove(word)

        return False

solution = Solution()
bo = solution.wordPatternMatch("abac", "abcuseabcblue")
print(bo)