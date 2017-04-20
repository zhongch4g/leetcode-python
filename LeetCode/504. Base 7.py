#-*-coding:utf-8 -*-
"""
    504. Base 7
    Directed by user zhongch4g
    current system date 2017/4/20
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 给定一个数num，返回一个7进制的数，用字符串表示
        # 有两种情况1.num为正数 2.num为负数
        # 开始先判断num为正还是为负
        # Note: The input will be in range of [-1e7, 1e7]. !!!  可能要转成字符串计算
        poOrna = 1
        if num < 0:
            poOrna = 0
            num = 0 - num
        s = ""
        if num == 0:
            return '0'
        while num > 0:
            st = (num % 7)
            s = s + str(st)
            num = (num - (st))/7
        if poOrna == 0:
            s = s + "-"
        return s[::-1]

        # 递归解法
        # if num < 0: return '-' + self.convertTo7(-num)
        # if num < 7: return str(num)
        # return self.convertTo7(num // 7) + str(num % 7)

instance = Solution()
print instance.convertToBase7(0)