#-*-coding:utf-8 -*-
"""
    231. Power of Two
    Directed by user zhongch4g
    current system date 2017/5/1
"""
import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        the = str(math.log(n, 2))
        split1, split2 = the.split(".")
        if split2 == '0':
            return True
        else:
            return False

        # 因为是求是否是2的幂数，可以用二进制判断，由于二进制中2的特殊性，即只要是二的幂数，其二进制中必然只有一个1
        # return n> 0 and bin(n).count('1') == 1


instance = Solution()
print instance.isPowerOfTwo(33)
