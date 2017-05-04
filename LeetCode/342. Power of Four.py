#-*-coding:utf-8 -*-
"""
    342. Power of Four
    Directed by user zhongch4g
    current system date 2017/5/4
"""
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        the = str(math.log(num, 4))
        split1, split2 = the.split(".")
        if split2 == '0':
            return True
        else:
            return False

instance = Solution()
print instance.isPowerOfFour(16)
