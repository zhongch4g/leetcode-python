#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 3:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : matrix_path.py
# @Software: IntelliJ IDEA


"""
dfs的题，找出0 1 matrix中是否存在从第一行到最后一行的路径，1才能通过

follow up1:输出任意路径

follow up2: 输出最短路径

口诉follow up：matrix中的的非零元素代表difficulty， 找出difficulty总和最小的路径。
"""

# Q1 是否存在

class Solution:
    def is_exist_valid_path(self, mat):
        if not mat:
            return False
        if not mat[0]:
            return False
        m, n = len(mat), len(mat[0])
        for i in range(n):
            if mat[0][i] == 0:
                if self.search_dfs(mat, 0, i, {(0, i)}):
                    return True
        return False

    def search_dfs(self, mat, i, j, visited):

        if i == len(mat) - 1 and mat[i][j] == 0:
            return True
        # 3 position
        result = False
        for _x, _y in [(0, 1), (1, 1), (1, -1)]:
            x, y = i + _x, j + _y
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]):
                continue
            if mat[i][j] == 1:
                continue
            if (x, y) in visited:
                continue

            visited.add((x, y))
            result = result or self.search_dfs(mat, x, y, visited)
            visited.remove((x, y))
        return result


# Q2
class Solution1:
    def get_arbitrary_path(self, mat):
        if not mat:
            return False
        if not mat[0]:
            return False
        m, n = len(mat), len(mat[0])
        paths = []
        for i in range(n):
            if mat[0][i] == 0:
                if self.search_dfs(mat, 0, i, {(0, i)}, paths, [(0, i)]):
                    print(paths)
                    return True
        return False

    def search_dfs(self, mat, i, j, visited, paths, path):

        if i == len(mat) - 1 and mat[i][j] == 0:
            paths.append(list(path))
            return True
        # 3 position
        result = False
        for _x, _y in [(0, 1), (1, 1), (1, -1)]:
            x, y = i + _x, j + _y
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]):
                continue
            if mat[i][j] == 1:
                continue
            if (x, y) in visited:
                continue

            visited.add((x, y))
            path.append((x, y))
            result = result or self.search_dfs(mat, x, y, visited, paths, path)
            path.pop()
            visited.remove((x, y))
        return result

from collections import deque
class Solution2:
    def get_minimum_path(self, mat):
        m, n = len(mat), len(mat[0])
        queue = deque([])
        # find all start position
        for i in range(n):
            if mat[0][i] == 0:
                queue.append((0, i))

        # define topleft "TL"
        # define topright "TR"
        # define top "T"
        end = (None, None)
        while queue:
            x, y = queue.popleft()
            if x == m - 1:
                end = (x, y)
                break
            if x + 1 < m and mat[x + 1][y] == 0:
                queue.append((x + 1, y))
                mat[x + 1][y] = "T"
            if x + 1 < m and y + 1 < n and mat[x + 1][y + 1] == 0:
                queue.append((x + 1, y + 1))
                mat[x + 1][y + 1] = "TL"
            if x + 1 < m and y - 1 >= 0 and mat[x + 1][y - 1] == 0:
                queue.append((x + 1, y - 1))
                mat[x + 1][y - 1] = "TR"

        if end == (None, None):
            return "Can't find path.."

        # from end to find shortest path
        path = [end]
        i, j = end
        while i != 0:
            if mat[i][j] == "T":
                i -= 1
                path.append((i, j))
            elif mat[i][j] == "TL":
                i -= 1
                j -= 1
                path.append((i, j))
            elif mat[i][j] == "TR":
                i -= 1
                j += 1
        path = reversed(path)
        print(list(path))
        return path




matrix = [[0, 1, 1, 1, 0],
          [1, 0, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0]]
solution = Solution()
res = solution.is_exist_valid_path(matrix)
print(res)


solution1 = Solution1()
solution1.get_arbitrary_path(matrix)


solution2 = Solution2()
solution2.get_minimum_path(matrix)