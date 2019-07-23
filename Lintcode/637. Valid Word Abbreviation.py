#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 1:51 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 637. Valid Word Abbreviation.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # edge case
        if not word and not abbr:
            return True
        if not word or not abbr:
            return False

        index1, index2 = 0, 0
        while index1 < len(word) and index2 < len(abbr):
            if abbr[index2] == word[index1]:
                index2 += 1
                index1 += 1
            else:
                if not '0' <= abbr[index2] <= '9':
                    return False
                total = 0
                while index2 < len(abbr) and '0' <= abbr[index2] <= '9':
                    if total == 0 and abbr[index2] == '0':
                        return False
                    total = total * 10 + int(abbr[index2])
                    index2 += 1
                index1 += total
                if index1 > len(word):
                    return False

                if index1 < len(word) and index2 < len(abbr) and word[index1] != abbr[index2]:
                    return False


        if index1 < len(word) or index2 < len(abbr):
            return False

        return True


s = "abbbbbbba"
abbr = "a7a"
solution = Solution()
res = solution.validWordAbbreviation(s, abbr)
print(res)