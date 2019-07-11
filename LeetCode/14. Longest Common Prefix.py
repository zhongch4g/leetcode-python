#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 6:57 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 14. Longest Common Prefix.py
# @Software: IntelliJ IDEA


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        comm_pre = ''
        cur = ''
        index = 0
        flag = 0

        while 1:
            for str in strs:

                if len(str) <= index:
                    if len(comm_pre):
                        return comm_pre
                    return comm_pre

                if flag == 0:
                    cur = str[index]
                    flag = 1

                if str[index] != cur:
                    return comm_pre

            comm_pre += cur
            index += 1
            flag = 0


solution = Solution()
res = solution.longestCommonPrefix([])
print(res)