#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 6:36 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 771. Jewels and Stones.py
# @Software: IntelliJ IDEA


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S or J == "" or S == "":
            return 0

        count = 0
        jewels = set(J)
        for c in S:
            if c not in jewels:
                continue
            count += 1
        return count
