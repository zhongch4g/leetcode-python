#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 11:27 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : watering_plants.py
# @Software: IntelliJ IDEA


class Solution:
    def watering_plants(self, plants, capacity):
        # edge case
        if not plants:
            return 0

        step = 0
        watering_position = 0
        while watering_position < len(plants):
            refill = capacity
            while watering_position < len(plants) and plants[watering_position] <= refill:
                refill -= plants[watering_position]
                watering_position += 1
            if watering_position == len(plants):
                step += watering_position
            else:
                step += watering_position * 2
        return step



solution = Solution()
res = solution.watering_plants([2], 3)
print(res)