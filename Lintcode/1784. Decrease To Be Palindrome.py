#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 11:30 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1784. Decrease To Be Palindrome.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        if not s:
            return 0

        p1, p2 = 0, len(s) - 1
        count = 0
        while p1 < p2:
            if ord(s[p1]) < ord(s[p2]):
                count += ord(s[p2]) - ord(s[p1])

            elif ord(s[p1]) > ord(s[p2]):
                count += ord(s[p1]) - ord(s[p2])
            p1 += 1
            p2 -= 1
        return count


solution = Solution()
solution.numberOfOperations("abc")

