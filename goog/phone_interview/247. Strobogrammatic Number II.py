#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 11:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 247. Strobogrammatic Number II.py
# @Software: IntelliJ IDEA


class Solution:
    def findStrobogrammatic(self, n: int):
        d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        ret = []
        # odd length, middle should be 0 or 1 or 8
        if n % 2 == 1:
            for s in ["0", "1", "8"]:
                self.dfs(s, d, n, ret)
        else:
            self.dfs("", d, n, ret)

        return ret

    def dfs(self, s, d, n, ret):
        if len(s) == n:
            ret.append(s)
        else:
            if len(s) == n - 2:
                for x in ["1", "6", "8", "9"]:
                    self.dfs(x+s+d[x], d, n, ret)
            else:
                for x in ["0", "1", "6", "8", "9"]:
                    self.dfs(x+s+d[x], d, n, ret)