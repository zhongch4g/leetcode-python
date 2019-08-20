#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 8:27 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 253. Meeting Rooms II.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        times = []
        for start, end in intervals:
            times.append((1, start))
            times.append((0, end))
        times.sort(key = lambda interval: (interval[1], interval[0]))
        minimum = - sys.maxsize - 1
        cur_room = 0
        for flag, time in times:
            if flag == 1:
                cur_room += 1
            if flag == 0:
                cur_room -= 1
            minimum = max(minimum, cur_room)
        return minimum