#-*-coding:utf-8 -*-
"""
    # @File    : 598. Range Addition II.py
    # @Author  : zhongch4g
    # @Time    : 2017/10/30 15:52
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # 通过面积决定包含的最大数个数

        # 找最小边界（配合m, n）
        minM = 40001
        minN = 40001
        for mtx in ops:
            if mtx[0] < minM:
                minM = mtx[0]
            if mtx[1] < minN:
                minN = mtx[1]
        return min(minM, m) * min(minN, n)


ops = [[2, 2], [3, 3]]
instance = Solution()
print(instance.maxCount(3, 3, ops))