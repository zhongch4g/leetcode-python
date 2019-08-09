#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 9:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 120. Word Ladder.py
# @Software: IntelliJ IDEA

from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = deque([start])
        distance = {start: 1}

        while queue:
            curr = queue.popleft()

            if curr == end:
                return distance[end]

            for next in self.get_next(curr):
                if next not in dict or next in distance:
                    continue
                queue.append(next)
                distance[next] = distance[curr] + 1
        return 0


    def get_next(self, word):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                temp = word[:i] + c + word[i + 1:]
                if temp == word:
                    continue
                words.append(temp)
        return words





start = "a"
end = "c"
d ={"a","b","c"}
solution = Solution()
solution.ladderLength(start, end, d)