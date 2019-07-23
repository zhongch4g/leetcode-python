#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 8:36 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 200. Number of Islands.py
# @Software: IntelliJ IDEA


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                self.search(grid, i, j)
                count += 1
        print(count)
        return count

    def search(self, grid, i, j):
        if grid[i][j] != '1':
            return
        grid[i][j] = '0'
        for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            _x, _y = i + step[0], j + step[1]
            if 0 <= _x < len(grid) and 0 <= _y < len(grid[0]):
                self.search(grid, _x, _y)





grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]

grid2 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
solution = Solution()
solution.numIslands(grid2)