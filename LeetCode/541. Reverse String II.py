#-*-coding:utf-8 -*-
"""
    541. Reverse String II
    Directed by user zhongch4g
    current system date 2017/4/26
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse(string):
            """
            :type string: str
            :rtype: str
            """
            return string[::-1]
        length = len(s)
        if k > length:
            return reverse(s)
        elif k < length and 2 * k > length:
            return reverse(s[:k]) + s[k:]
        else:
            return reverse(s[:k]) + s[k:2 * k] + self.reverseStr(s[2 * k:], k)

instance = Solution()
# print instance.reverseStr("abcdefg", 2)
print instance.reverseStr("abcdefg", 3)
print instance.reverseStr("abc", 4)
print instance.reverseStr("abcdh", 4)