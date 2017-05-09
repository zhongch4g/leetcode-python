#-*-coding:utf-8 -*-
"""
    70. Climbing Stairs
    Directed by user zhongch4g
    current system date 2017/5/2
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)



instance = Solution()
print instance.climbStairs(35)