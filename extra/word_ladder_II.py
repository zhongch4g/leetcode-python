#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 1:00 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_ladder_II.py
# @Software: IntelliJ IDEA

from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        results = []
        # set distance
        distance = {}
        self.bfs(end, start, distance, dict)

        # find path
        self.dfs(start, end, distance, dict, [start], results)
        print(results)

    def get_next(self, word, dictionary):
        next_words = []
        for i in range(len(word)):
            for j in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + j + word[i + 1:]
                if next_word == word or next_word not in dictionary:
                    continue
                next_words.append(next_word)
        return next_words

    def bfs(self, start, end, distance, dictionary):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next(word, dictionary):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def dfs(self, start, end, distance, dictionary, path, results):
        if start == end:
            results.append(list(path))
            return

        for next_word in self.get_next(start, dictionary):
            # 防止end不在搜索的那一侧树
            if distance[next_word] != distance[start] - 1:
                continue

            path.append(next_word)
            self.dfs(next_word, end, distance, dictionary, path, results)
            path.pop()


# Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
dict = set(["hot","dot","dog","lot","log"])
solution = Solution()
solution.findLadders("hit", "cog", dict)