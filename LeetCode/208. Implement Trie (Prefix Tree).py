#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 12:34 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 208. Implement Trie (Prefix Tree).py
# @Software: IntelliJ IDEA


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True
        # trie['#'] = word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        if 'end' in t:
            return True
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)