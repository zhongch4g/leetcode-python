#-*-coding:utf-8 -*-
"""
    242. Valid Anagram
    Directed by user zhongch4g
    current system date 2017/4/20
"""
import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s1 = collections.Counter(s)
        # s2 = collections.Counter(t)
        # return s1 == s2
        # return collections.Counter(s) == collections.Counter(t)
        # return sorted(s) == sorted(t)

        # 经过对比程序测试时长，发现字典要比排序更快
        # dict.get(key, default=None)
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2


instance = Solution()
print instance.isAnagram("anagram", "nagaram")
print instance.isAnagram("car", "acr")