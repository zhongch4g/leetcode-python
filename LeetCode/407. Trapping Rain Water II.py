#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 10:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 407. Trapping Rain Water II.py
# @Software: IntelliJ IDEA


import heapq
class Solution:
    def trapRainWater(self, heightMap) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        water = 0
        heap = []
        visited = set()
        # add edge position into heap to find smallest
        for i in range(len(heightMap)):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, \
                           (heightMap[i][len(heightMap[0]) - 1], i, len(heightMap[0]) - 1))

            visited.add((i, 0))
            visited.add((i, len(heightMap[0]) - 1))
        for j in range(len(heightMap[0])):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, \
                           (heightMap[len(heightMap) - 1][j], len(heightMap) - 1, j))

            visited.add((0, j))
            visited.add((len(heightMap) - 1, j))

        # find the smallest height and watering
        while heap:
            smallest_height, x, y = heapq.heappop(heap)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                _x = x + i
                _y = y + j
                if _x < 0 or _x >= len(heightMap) or _y < 0 or _y >= len(heightMap[0]) or (_x, _y) in visited:
                    continue
                visited.add((_x, _y))
                if smallest_height > heightMap[_x][_y]:
                    water += smallest_height - heightMap[_x][_y]
                    heapq.heappush(heap, (smallest_height, _x, _y))
                else:
                    heapq.heappush(heap, (heightMap[_x][_y], _x, _y))
        return water



