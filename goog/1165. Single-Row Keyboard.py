#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 7:15 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1165. Single-Row Keyboard.py
# @Software: IntelliJ IDEA


class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """

        char_position = {}
        for i in range(26):
            char_position[keyboard[i]] = i

        start = 0
        step = 0
        for c in word:
            step += abs(char_position[c] - start)
            start = char_position[c]
        return step