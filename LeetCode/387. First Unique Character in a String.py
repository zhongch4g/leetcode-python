#-*-coding:utf-8 -*-
"""
    387. First Unique Character in a String
    Directed by user zhongch4g
    current system date 2017/4/17
"""
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符串判定，如果传入的字符串为空或不存在则返回-1
        if s is [] or s is None:
            return -1
        # 用collections.Counter()得到字符串中各个字母的个数统计
        s_num = collections.Counter(s)
        # 用index作为游标，拿到第一个字母字母统计为1的index，即为第一个non-repeating character
        for index in range(len(s)):
            # print s_num[s[index]]
            if s_num[s[index]] is 1:
                return index
        # 查找整个字符串后如果还没有结果则返回-1
        return -1


s1 = "leetcode" # return 0
s2 = "loveleetcode" # return 2
s3 = 'leetcode'
s4 = "aaaaaaaa"
s5 = "abcdefg"
instance = Solution()
print instance.firstUniqChar(s4)
print instance.firstUniqChar(s5)
# s = collections.Counter(s1)
# print type(s['e'])
