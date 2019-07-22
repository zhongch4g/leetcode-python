#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 2:05 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_squares.py
# @Software: IntelliJ IDEA

# define data structure
class TrieNode :
    def __init__(self) :
        self.children = {}
        self.is_word = False
        self.word_list = []

class Trie :
    def __init__(self) :
        self.root = TrieNode()

    def add(self, word) :
        node = self.root
        for c in word :
            if c not in node.children :
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word) :
        node = self.root
        for c in word :
            node = node.children.get(c)
            if node is None :
                return None
        return node

    def words_prefix(self, prefix) :
        node = self.find(prefix)
        return [] if node is None else node.word_list


class Solution:

    def wordSquares(self, words):
        # 初始化trie，加入单词
        trie = Trie()
        for word in words :
            trie.add(word)
        # 检测是否可以加入，sqaure为list
        squares = []
        for word in words :
            self.search(trie, [word], squares)

        return squares

    def search(self, trie, square, squares) :
        # eg. ['wall', 'area'] n: 单词长度 4, pos: 单词数目 2
        n, pos = len(square[0]), len(square)
        # 递归出口 - 需要deep copy
        if n == pos :
            squares.append(list(square))
            return

            # 剪枝 - 以后面为前缀的是否存在
        for col in range(pos, n) :
            prefix = ''.join(square[i][col] for i in range(pos))
            if trie.find(prefix) is None :
                return

                # ['wall',
        #  'area']  prefix = 'le'，下一个应该以le开头，每行的pos - 2
        prefix = ''.join(square[i][pos] for i in range(pos))
        for word in trie.words_prefix(prefix) :
            # 尝试将word加入
            square.append(word)
            self.search(trie, square, squares)
            square.pop()