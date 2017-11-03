#-*-coding:utf-8 -*-
"""
    # @File    : 628. Maximum Product of Three Numbers.py
    # @Author  : zhongch4g
    # @Time    : 2017/11/3 14:31
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 最大的乘积 ：
        # 找到最大的三个数和最小的两个数
        nums = sorted(nums)[::-1]
        m1, m2, m3 = nums[:3]
        min1, min2 = nums[-2:]
        # print(m1, m2, m3, min1, min2)

        return max(m1*m2*m3, min1*min2*m1)

    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx1 = -1001
        mx2 = -1001
        mx3 = -1001
        mn1 = 1001
        mn2 = 1001
        for n in nums:
            if n > mx3:
                mx3 = mx2
                if n > mx2:
                    mx2 = mx1
                    if n > mx1:
                        mx1 = n
                    else:
                        mx2 = n
                else:
                    mx3 = n
            if n < mn2:
                mn2 = mn1
                if n < mn1:
                    mn1 = n
                else:
                    mn2 = n
        return max(mx1 * mx2 * mx3, mx1 * mn1 * mn2)


instance = Solution()
print(instance.maximumProduct1([1,2,3]))