#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 11:46 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1184. Distance Between Bus Stops.py
# @Software: IntelliJ IDEA


class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        if start == destination:
            return 0

        if not distance:
            return 0

        presum = [0]
        for dis in distance:
            presum.append(presum[-1] + dis)
        backsum = [0]
        for dis in range(len(distance) - 1, -1, -1):
            backsum.append(backsum[-1] + distance[dis])

        if start > destination:
            start, destination = destination, start

        pre = presum[destination] - presum[start]
        back = presum[start] - presum[0] + backsum[len(distance) - destination] - backsum[0]
        # print(pre, back)
        return pre if pre < back else back

        # 17