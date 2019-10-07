#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 10:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : stream_find_word_index.py
# @Software: IntelliJ IDEA

"""
Stream: backiuwcatbeforewerehpqojf
Input: ["back", "before", "cat", fore", "were", "for"]
Output: [0, 10, 7, 12, 16, 12]
Generator: char getNextChar();

给一个random stream，只能用getNextChar();获取下一个char，
给一个list of input words，找每个word在stream中出现的位置（出现位置）
假设stream够长，即使是‍‍‌‌‍‌‌‌‌‍‍‍‌‍‍‌‍‌‍random，也一定会出现每个word

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.index = None
        self.length = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word, i, length):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True
        node.index = i
        node.length = length

class Solution:
    def __init__(self):
        self.index = -1
        self.stream = "backiuwcatbeforewerehpqojf"
        # self.stream = "bebefore"

    def getNextChar(self):
        if self.index + 1 < len(self.stream):
            self.index += 1
            return self.stream[self.index]
        else:
            return None

    def stream_find_word_index(self, strs):

        trie = Trie()
        # create Trie for input strs
        for i, s in enumerate(strs):
            trie.insert(s, i, len(s))
        node = trie.root
        list_of_trie_node = []
        list_of_trie_node_next = [node]
        result = [None for i in range(len(strs))]
        count = 0
        idx = 0

        while count <= len(strs):
            list_of_trie_node = list_of_trie_node_next
            list_of_trie_node_next = []
            char = self.getNextChar()
            if not char:
                break
            for tn in list_of_trie_node:
                if char not in tn.children:
                    continue
                if tn.children[char].is_word:
                    result[tn.children[char].index] = idx - tn.children[char].length + 1
                    count += 1
                list_of_trie_node_next.append(tn.children[char])

            # add root
            list_of_trie_node_next.append(node)

            idx += 1
        print(result)
        return result


solution = Solution()
solution.stream_find_word_index(["back", "before", "cat", "fore", "were", "for"])
# solution.stream_find_word_index(["before", "fore"]) # "bebefore"
# Output: [0, 10, 7, 12, 16, 12]
# Generator: char getNextChar();