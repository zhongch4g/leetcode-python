#-*-coding:utf-8 -*-
"""
    367. Valid Perfect Square
    Directed by user zhongch4g
    current system date 2017/5/6
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 1 4 16 25 36
        # 对于一个整数 n，它的平方写成 n2。n2等于头 n 个正奇数的和

        # l, r=1, num
        #
        # while l<=r:
        #     m= (l+r)/2
        #     if m*m== num:
        #         return True
        #     elif m*m<num:
        #         l=m+1
        #     else:
        #         r=m-1
        # return False

        n = 1
        while n*n<=num:
            n += 1
        if n**2 == num or (n-1)**2 == num:
            return True
        else:
            return False


instance = Solution()
print instance.isPerfectSquare(25)
