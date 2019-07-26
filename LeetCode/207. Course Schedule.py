#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 12:06 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 207. Course Schedule.py
# @Software: IntelliJ IDEA
from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = {}
        neighbor = {}
        for i in range(numCourses):
            indegree[i] = indegree.get(i, 0)
            neighbor[i] = neighbor.get(i, [])
        for pre in prerequisites:
            if pre[0] in indegree:
                indegree[pre[0]] += 1
            if pre[1] in neighbor:
                neighbor[pre[1]].append(pre[0])

        queue = deque()
        # res = []
        res = 0
        # init
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            cur = queue.popleft()
            res += 1
            for n in neighbor[cur]:
                if n in indegree:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)

        if res == numCourses:
            return True
        return False


solution = Solution()
res = solution.canFinish(2, [[1, 0]])
print(res)