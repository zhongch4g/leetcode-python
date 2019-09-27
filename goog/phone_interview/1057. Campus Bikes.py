#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 3:13 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1057. Campus Bikes.py
# @Software: IntelliJ IDEA


"""
狗高频：人车匹配

LC里的给的样例是两个数组，workers 和 bikes，返回一个ans，索引对应worker 值对应bike

普遍的人车匹配会给你一个2D grid，

"""

import sys
import collections
class Solution:
    def assignBikes(self, workers, bikes):

        w = len(workers)
        b = len(bikes)
        unvisitedw = set()
        unvisitedb = set()

        for i in range(w):
            unvisitedw.add(i)

        for j in range(b):
            unvisitedb.add(j)

        dist = collections.defaultdict(list)
        # set distance as key to match (i, j) pair
        for i in range(w):
            for j in range(b):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                dist[distance].append((i, j))

        res = [-sys.maxsize - 1] * w
        for i in range(1, 2001):
            pairs = dist.get(i, None)
            if not pairs:
                continue
            for pw, pb in pairs:
                if pw in unvisitedw and pb in unvisitedb:
                    res[pw] = pb
                    unvisitedw.remove(pw)
                    unvisitedb.remove(pb)
        return res


"""
给一个2D grid，上面有position of same number of people and bikes, 
并且已知我在哪个位置。求我去哪个自行车，可以保证能够拿到车（保证这台车不会被别人抢先）
"""
import math
class Solution2:
    def assignBikes(self, grid, location):
        location = (location[0], location[1])
        row = len(grid)
        col = len(grid[0])
        workers = []
        bikes = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'W':
                    workers.append((row - 1 - i, j))
                if grid[i][j] == 'B':
                    bikes.append((row - 1 - i, j))
        # print(workers)
        # print(bikes)
        unvisitedw = set()
        unvisitedb = set()
        for worker in workers:
            unvisitedw.add((worker[0], worker[1]))

        for bike in bikes:
            unvisitedb.add((bike[0], bike[1]))

        # calculate distance
        # this order to store dist just for match the problem
        # when workers has same distance to bike, select low index worker
        # when multiple way(same distance to more than 2 bikes)
        dist = collections.defaultdict(list)
        for bike in bikes:
            for work in workers:
                distance = math.sqrt((bike[0] - work[0]) ** 2 + (bike[1] - work[1]) ** 2)
                dist[distance].append([(bike[0], bike[1]), (work[0], work[1])])
        # print(dist)
        for i in range(2001):
            pairs = dist.get(i, None)
            if not pairs:
                continue
            for pair in pairs:
                if pair[0] in unvisitedb and pair[1] in unvisitedw:
                    # print(pair[1], location)
                    if pair[1] == location:
                        print(pair[0])
                        return pair[0]
                    unvisitedb.remove(pair[0])
                    unvisitedw.remove(pair[1])
        print("can't find the match bike...")
        return None


grid = [['0', '0', 'B'],
        ['0', 'W', 'B'],
        ['W', 'B', 'W']]
s = Solution2()
s.assignBikes(grid, [1, 1])