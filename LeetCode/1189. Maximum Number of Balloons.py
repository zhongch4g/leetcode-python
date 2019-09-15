#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 11:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1189. Maximum Number of Balloons.py
# @Software: IntelliJ IDEA


import sys
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        max_balloons = sys.maxsize
        balloons = [0 for i in range(26)]

        count = 0
        for c in text:
            if c in "balloon":
                balloons[ord(c) - ord('a')] += 1

        l1 = [ord('b') - ord('a'), ord('a') - ord('a'), ord('n') - ord('a')]
        l2 = [ord('l') - ord('a'), ord('o') - ord('a')]
        print(balloons)
        for i in range(len(balloons)):
            if i in l1:
                max_balloons = min(max_balloons, balloons[i])
            if i in l2:
                max_balloons = min(max_balloons, balloons[i]//2)

        return max_balloons if max_balloons != sys.maxsize else 0
