#-*-coding:utf-8 -*-
"""
    118. Pascal's Triangle
    Directed by user zhongch4g
    current system date 2017/5/8
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows > 2:
            init = [[1], [1, 1]]
            for i in range(2, numRows):
                plus = []
                pre = init[i - 1]
                for x in range(i + 1):  #
                    if (x - 1) < 0 or x + 1 > i:
                        plus.append(1)
                    else:
                        plus.append(pre[x - 1] + pre[x])
                init.append(plus)
        return init

        # One simple solution
        # res = [[1] for i in range(numRows)]
        # for n in range(1, numRows):
        #     for i in range(1, n):
        #         res[n].append(res[n-1][i-1] + res[n-1][i])
        #     res[n].append(1)
        # return res

instance = Solution()
print instance.generate(5)
