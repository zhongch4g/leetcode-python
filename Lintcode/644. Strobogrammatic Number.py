#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 2:53 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 644. Strobogrammatic Number.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):

        mirror = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        i, j = 0, len(num) - 1
        while i < j:
            if num[i] in mirror and num[j] in mirror:
                if num[i] == mirror[num[j]]:
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                return False



        if i == j and num[i] not in ['0', '1', '8']:
            return False

        return True

