#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 12:01 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 648. Unique Word Abbreviation.py
# @Software: IntelliJ IDEA


class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.dictionary = dictionary

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        # construct abbr list
        abbr = {}
        count = {}
        for w in self.dictionary:
            w_abbr = self.get_abbr(w)
            abbr[w_abbr] = abbr.get(w_abbr, 0) + 1
            count[w] = count.get(w, 0) + 1

        a = self.get_abbr(word)
        if count.get(word, 0) == abbr.get(a, 0):
            return True
        return False

    def get_abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

vw = ValidWordAbbr(["a", "a"])
res = vw.isUnique('a')
print(res)


    # Your ValidWordAbbr object will be instantiated and called as such:
    # obj = ValidWordAbbr(dictionary)
    # param = obj.isUnique(word)