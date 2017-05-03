#-*-coding:utf-8 -*-
"""
    263. Ugly Number
    Directed by user zhongch4g
    current system date 2017/5/3
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp = num
        if num % 2 == 0:
            num = num / 2
        if num % 3 == 0:
            num = num / 3
        if num % 5 == 0:
            num = num / 5
        if temp == num:
            if num == 1:
                return True
            else:
                return False
        return self.isUgly(num)

instance = Solution()
print instance.isUgly(8)
