#-*-coding:utf-8 -*-
"""
    326. Power of Three
    Directed by user zhongch4g
    current system date 2017/4/29
"""
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        the = str(math.log(n, 3))
        split1, split2 = the.split(".")
        if split2 == '0':
            return True
        else:
            return False


instance = Solution()
print instance.isPowerOfThree(-9)

for i in range(25):
    print i, 3**i
