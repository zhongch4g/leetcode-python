#-*-coding:utf-8 -*-
"""
    66. Plus One
    Directed by user zhongch4g
    current system date 2017/5/5
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 题目大意：模拟数字加一的过程
        remainder = 1
        for i in range(len(digits))[::-1]:
            if remainder == 1:
                digits[i] += 1
                remainder = 0
            if digits[i] >= 10:
                remainder = 1
                digits[i] = digits[i] % 10
            if i == 0 and remainder == 1:
                digits.insert(0, 1)
        return digits

instance = Solution()
print (instance.plusOne([7, 9]))