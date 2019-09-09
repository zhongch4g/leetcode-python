#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 6:19 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 332. Reconstruct Itinerary.py
# @Software: IntelliJ IDEA

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


solution = Solution()
solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])