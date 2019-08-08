#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 1:09 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 794. Sliding Puzzle II.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):

        if not init_state or not final_state:
            return -1

        source = self.list_to_str(init_state)
        target = self.list_to_str(final_state)
        queue = deque([source])
        visited = {source}
        step = 0
        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == target:
                    return step

                for next in self.get_next(curr):
                    if next in visited:
                        continue
                    queue.append(next)
                    visited.add(next)

            step += 1
        return -1


    def get_next(self, state: str) -> list:
        states = []
        zero_idx = state.index('0')
        x = zero_idx // 3
        y = zero_idx % 3

        # find other state
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            _x, _y = x + i, y + j
            if not self.is_valid_position(_x, _y):
                continue

            chars = list(state)
            chars[x * 3 + y] = chars[_x * 3 + _y]
            chars[_x * 3 + _y] = '0'
            states.append(''.join(chars))
        return states


    def is_valid_position(self, i, j):
        return 0 <= i < 3 and 0 <= j < 3


    def list_to_str(self, state):
        string = ''
        for row in state:
            for j in row:
                string += str(j)
        return string


# 283104765
# 5%3 = 2
# 5/3 = 1
init_state = [
                [2,8,3],
                [1,0,4],
                [7,6,5]]
final_state = [
                [1,2,3],
                [8,0,4],
                [7,6,5]]

solution = Solution()
res = solution.minMoveStep(init_state, final_state)
print(res)