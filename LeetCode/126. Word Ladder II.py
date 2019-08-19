#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 12:06 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 126. Word Ladder II.py
# @Software: IntelliJ IDEA


# TLE
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):

        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []
        wordList = set(wordList)
        # 1. shortest distance
        distance = self.bfs(endWord, beginWord, wordList)
        print(distance)
        # 2. all path in range of distance
        all_path = []
        if distance == -1:
            return all_path
        self.dfs(beginWord, endWord, wordList, 0, distance, [beginWord], all_path, {beginWord})

        return all_path

    def dfs(self, start, end, wordList, index, distance, path, all_path, visited):
        if index >= distance:
            return
        if end in path:
            all_path.append(list(path))
            return

        for word in self.get_next(start):
            if word not in wordList or word in visited:
                continue

            path.append(word)
            visited.add(word)
            self.dfs(word, end, wordList, index + 1, distance, path, all_path, visited)
            path.pop()
            visited.remove(word)


    def bfs(self, start, end, wordList):

        distance = 1
        wordList.add(end)
        queue = deque([start])
        visited = {start}

        while queue:

            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == end:
                    return distance

                for word in self.get_next(cur):
                    if word in wordList and word not in visited:
                        queue.append(word)

            distance += 1
        return -1

    def get_next(self, word):
        next_word = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i + 1:]
                if new == word:
                    continue
                next_word.append(new)
        return next_word


# accept
from collections import deque
class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList):

        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []
        wordList = set(wordList)
        # 1. shortest distance
        distance = {}
        self.bfs(endWord, beginWord, distance, wordList)
        print(distance)
        # 2. all path in range of distance
        all_path = []
        if distance == -1:
            return all_path
        self.dfs(beginWord, endWord, wordList, distance, [beginWord], all_path)

        return all_path

    def dfs(self, start, end, wordList, distance, path, all_path):
        if start == end:
            all_path.append(list(path))
            return

        for word in self.get_next(start, wordList):
            if distance[word] != distance[start] - 1:
                continue

            path.append(word)
            self.dfs(word, end, wordList, distance, path, all_path)
            path.pop()


    def bfs(self, start, end, distance, wordList):

        distance[start] = 0
        wordList.add(end)
        queue = deque([start])

        while queue:
            cur = queue.popleft()

            for word in self.get_next(cur, wordList):
                if word not in distance:
                    queue.append(word)
                    distance[word] = distance[cur] + 1

        return -1

    def get_next(self, word, wordList):
        next_word = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i + 1:]
                if new != word and new in wordList:
                    next_word.append(new)
        return next_word













