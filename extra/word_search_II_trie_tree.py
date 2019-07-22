#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 11:35 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_search_II_trie_tree.py
# @Software: IntelliJ IDEA

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_word = True
        node.word = word

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get[c]
            if node is None:
                return None
        return node

    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    def start_with(self, word):
        node = self.find(word)
        return node is not None


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if not words or not board:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(board, i, j, set(), trie.root.children.get(c), [], result)
        return result


    def search(self, board, i, j, visited, node, cur_word, result):
        if node is None:
            return

        if node.is_word:
            result.add(node.word)

        for delta_x, delta_y in DIRECTIONS:

            _x = i + delta_x
            _y = j + delta_y

            if not self.is_valid(board, _x, _y):
                continue

            if (_x, _y) in visited:
                continue

            visited.add((i, j))
            self.search(board, _x, _y, visited, node.children.get(board[_x][_y]), cur_word, result)
            visited.remove((i, j))


    def is_valid(self, board, i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]
output = ["again","can","dad","dog"]

solution = Solution()
result = solution.wordSearchII(board, words)
print(result)