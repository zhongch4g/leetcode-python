#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:10 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : distance_of_string.py
# @Software: IntelliJ IDEA

"""

两个字符串的距离定义为除去共同前缀后两字符串长度只和。给一个二元字符串列表，请给出距离最大的两个字符串的距离。
"""

class TrieNode:
    def __init__(self, depth):
        # self.char = char
        self.left = None
        self.right = None
        self.isEnd = False
        self.depth = depth

    def get(self, c):
        if c == '1':
            return self.right
        else:
            return self.left

    def set(self, c):
        if c == '1':
            self.right = TrieNode(self.depth + 1)
        else:
            self.left = TrieNode(self.depth + 1)

    def getDepth(self):
        leftDepth = self.depth
        rightDepth = self.depth
        if self.left: leftDepth = self.left.getDepth()
        if self.right: rightDepth = self.right.getDepth()
        return max(leftDepth, rightDepth)

    def maxDistance(self):
        if self.right and self.left: return self.left.getDepth() + self.right.getDepth() - self.depth * 2
        if self.left: return self.left.maxDistance()
        if self.right: return self.right.maxDistance()
        return 0


class BinaryTrie:
    def __init__(self):
        self.root = TrieNode(0)

    def insert(self, s):
        node = self.root
        for c in s:
            cur = node.get(c)
            if not cur:
                node.set(c)
            node = node.get(c)
        node.isEnd = True

    def search(self, s):
        node = self.root
        for c in s:
            node = node.get(c)
            if not node: return False
        return node.isEnd


class Test:

    def setup(self, words):
        self.trie = BinaryTrie()
        for word in words:
            self.trie.insert(word)

    def test1(self):
        words = ['1011000', '10111101', '1100000']
        # words = ['abcqqq', 'abqqq', 'zww']
        self.setup(words)
        distance = self.trie.root.maxDistance()
        print('max_distance between words ', words, distance)

test = Test()
test.test1()


class Solution:
    def max_distance(self, words):
        trie = {'depth': 0}
        for word in words:
            cur_trie = trie
            for c in word:
                if c not in cur_trie:
                    cur_trie[c] = {'depth': cur_trie['depth'] + 1}
                cur_trie = cur_trie[c]




words = ['1011000', '10111101', '1100000']
solution = Solution()
solution.max_distance(words)