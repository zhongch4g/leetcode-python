#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 8:58 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 612. K Closest Points.py
# @Software: IntelliJ IDEA
import math


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# class NewPoint(Point):
#     def __lt__(self, other):
#         return (self.x, self.y) < (other.x, other.y)

import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):

        heap = []
        for point in points:
            dis = math.sqrt((point.x - origin.x)**2 + (point.y - origin.y)**2)
            heapq.heappush(heap, (-dis, -point.x, -point.y))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            _, x, y = heapq.heappop(heap)
            result.append(Point(-x, -y))
        result.reverse()
        return result


    def kClosest2(self, points, origin, k):
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))

        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


points = [Point(4,6),Point(4,6),Point(4,6),Point(-4,-6),Point(-4,6)]
origin = Point(0,0)
k = 3
solution = Solution()
solution.kClosest(points, origin, k)
