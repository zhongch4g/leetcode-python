#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 12:56 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 639. Word Abbreviation.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        ans = [0] * len(dict)
        abbr = {}
        round = 1
        for i in range(len(dict)):
            ans[i] = self.get_abbr(dict[i], round)
            abbr[ans[i]] = abbr.get(ans[i], 0) + 1


        while True:
            unique = True
            round += 1
            for i in range(len(dict)):
                if abbr[ans[i]] > 1:
                    ans[i] = self.get_abbr(dict[i], round)
                    abbr[ans[i]] = abbr.get(ans[i], 0) + 1
                    unique = False
            if unique:
                break
        return ans


    def get_abbr(self, word, pre):
        if pre + 2 >= len(word):
            return word

        return word[:pre] + str(len(word) - pre - 1) + word[-1]
