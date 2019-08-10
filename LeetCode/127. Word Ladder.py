#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 7:21 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 127. Word Ladder.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # important
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        wordList = set(wordList)
        distance = {beginWord: 1}
        queue = deque([beginWord])

        while queue:
            cur_word = queue.popleft()

            if cur_word == endWord:
                return distance[endWord]

            for word in self.get_next(cur_word):
                if word not in wordList:
                    continue
                if word in distance:
                    continue
                queue.append(word)
                distance[word] = distance[cur_word] + 1
        return 0

    def get_next(self, word):
        words = []

        for i in range(len(word)):
            for j in "abcdefghijklmnopqrstuvwxyz":
                nword = word[:i] + j + word[i + 1:]
                if nword == word:
                    continue
                words.append(nword)
        return words