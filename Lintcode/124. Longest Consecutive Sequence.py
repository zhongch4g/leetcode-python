#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 12:50 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 124. Longest Consecutive Sequence.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):

        hash = set(num)
        length = - sys.maxsize - 1
        for n in num:
            if n not in hash:
                continue

            left, right = n - 1, n + 1

            while left in hash:
                hash.remove(left)
                left -= 1

            while right in hash:
                hash.remove(right)
                right += 1

            length = max(length, right - left - 1)
        return length