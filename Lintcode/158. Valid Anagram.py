#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 11:50 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 158. Valid Anagram.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        ss = [0] * 256
        st = [0] * 256
        for i in s:
            ss[ord(i)] += 1
        for j in t:
            st[ord(j)] += 1

        for i in range(256):
            if ss[i] != ss[i]:
                return False
        return True