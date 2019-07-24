#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 6:08 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 616. Course Schedule II.py
# @Software: IntelliJ IDEA

from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    # 时间复杂度过高
    def findOrder(self, numCourses, prerequisites):

        if not prerequisites:
            return [i for i in range(numCourses)]

        in_degree = {}
        result = []

        for i in range(numCourses):
            in_degree[i] = in_degree.get(i, 0)
        for rel in prerequisites:
            if rel[0] in in_degree:
                in_degree[rel[0]] += 1
        print(in_degree)

        ind_0 = []
        for node, ind in in_degree.items():
            if ind != 0:
                continue
            ind_0.append(node)
        queue = deque(ind_0)

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for rel in prerequisites:
                if rel[1] == curr:
                    in_degree[rel[0]] -= 1

                if in_degree[rel[0]] == 0:
                    queue.append(rel[0])
                    in_degree[rel[0]] = None
        if len(result) != numCourses:
            return []
        print(result)
        return result


    def findOrder2(self, numCourses, prerequisites):
        if not prerequisites:
            return [i for i in range(numCourses)]

        in_degree = {}
        edges = {i: [] for i in range(numCourses)}
        result = []
        for i in range(numCourses):
            in_degree[i] = in_degree.get(i, 0)

        for rel in prerequisites:
            in_degree[rel[0]] = in_degree.get(rel[0], 0) + 1
            edges[rel[1]].append(rel[0])

        queue = deque([])
        for node, ind in in_degree.items():
            if ind != 0:
                continue
            queue.append(node)

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for rel in edges[curr]:
                in_degree[rel] -= 1

                if in_degree[rel] == 0:
                    queue.append(rel)

        if len(result) != numCourses:
            return []
        print(result)
        return result


n = 2
prerequisites = [[1,0]]
solution = Solution()
solution.findOrder2(n, prerequisites)


