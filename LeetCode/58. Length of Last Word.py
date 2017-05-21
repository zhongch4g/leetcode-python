#-*-coding:utf-8 -*-
"""
    58. Length of Last Word
    Directed by user zhongch4g
    current system date 2017/5/21
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # list1 = s.strip(' ').split(' ')
        # return list1
        return len(s.strip(' ').split(' ')[-1])


instance = Solution()
print instance.lengthOfLastWord("Hello World")