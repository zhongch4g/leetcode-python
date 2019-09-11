#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 8:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1048. Longest String Chain.py
# @Software: IntelliJ IDEA


from collections import defaultdict, deque
class Solution:
    def longestStrChain(self, words) -> int:
        length = defaultdict(list)
        for word in words:
            length[len(word)].append(word)

        graph, start = self.get_graph(words, length)

        queue = deque([])
        for word in words:
            if start[word] > 0:
                continue
            queue.append(word)
        longest = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if graph[cur]:
                    queue += graph[cur]
            longest += 1
        return longest

    def get_graph(self, words, length):
        graph = defaultdict(list)
        keys = sorted(length.keys())
        start = defaultdict(int)
        for i in range(len(keys) - 1):
            if keys[i + 1] != keys[i] + 1:
                graph[i] = []
            else:
                for word1 in length[keys[i]]:
                    for word2 in length[keys[i + 1]]:
                        if self.judge(word1, word2):
                            start[word2] += 1
                            graph[word1].append(word2)
        return graph, start

    def judge(self, word1, word2):
        # word1 can be word2's predecessor or not
        if len(word1) + 1 != len(word2):
            return False

        i, j = 0, 0
        add = 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                j += 1
                add += 1
        # attention this corner case
        if add == 0 and i == len(word1) and j + 1 == len(word2):
            return True
        if add != 1:
            return False
        return True
