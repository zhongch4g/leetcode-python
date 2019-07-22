#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 4:27 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : Trie.py
# @Software: IntelliJ IDEA

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True

    """
    return the node in the trie if exists 
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def starts_with(self, prefix):
        return self.find(prefix) is not None