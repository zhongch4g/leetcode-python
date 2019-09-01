#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 12:19 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1176. Diet Plan Performance.py
# @Software: IntelliJ IDEA


class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        length = len(calories)
        if length == 0 or k == 0:
            return k
        r = 0
        cursum = 0
        day = 0
        points = 0
        for l in range(length):
            while r < length and day < k:
                cursum += calories[r]
                day += 1
                r += 1
            if day == k and cursum < lower:
                points -= 1
            if day == k and cursum > upper:
                points += 1

            cursum -= calories[l]
            day -= 1

        return points