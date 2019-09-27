#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 10:05 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1066. Campus Bikes II.py
# @Software: IntelliJ IDEA

# Memoization
class Solution:
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        w = len(workers)
        b = len(bikes)
        d = [[0 for i in range(w)] for j in range(b)]
        for i in range(b):
            for j in range(w):
                d[i][j] = abs(workers[j][0] - bikes[i][0]) + abs(workers[j][1] - bikes[i][1])
        visited = [0 for k in range(b)]
        return self.backtrack(0,visited,w,b,d,{})

    def backtrack(self,i,visited,w,b,d,my_dict):
        if i == w:
            return 0
        ans = 2**31-1
        if tuple(visited) in my_dict:
            ans = my_dict[tuple(visited)]
        else:
            for j in range(b):
                if not visited[j]:
                    visited[j] = 1
                    ans = min(ans,d[j][i] + self.backtrack(i+1,visited,w,b,d,my_dict))
                    visited[j] = 0
            my_dict[tuple(visited)] = ans
        return ans