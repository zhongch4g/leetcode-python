#-*-coding:utf-8 -*-
"""
    # @File    : 575. Distribute Candies.py
    # @Author  : zhongch4g
    # @Time    : 2017/10/30 15:16
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # allCandies = dict()
        # for i in candies:
        #     allCandies.setdefault(i, 0)
        #     allCandies[i] += 1
        a = len(set(candies))
        b = len(candies)
        if a <= (b / 2):
            return a
        else:
            return b / 2

instance = Solution()
instance.distributeCandies([1, 1, 2, 2, 3, 3])