#-*-coding:utf-8 -*-
"""
    500. Keyboard Row
    Directed by user zhongch4g
    current system date 2017/4/21
"""
import re


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        list = []
        for string in words:
            s1 = ""
            s2 = ""
            s3 = ""
            string1 = string.lower()
            for char in string1:
                if char in row1:
                    s1 += char
                if char in row2:
                    s2 += char
                if char in row3:
                    s3 += char
            # print s1, s2, s3
            if s1 == string1 or s2 == string1 or s3 == string1:
                list.append(string)
        return list
    # python 一行解法
    def findWords1(self, words):
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

instance = Solution()
print instance.findWords1(["Hello", "Alaska", "Dad", "Peace"]) # "Hello", "Alaska", "Dad", "Peace"