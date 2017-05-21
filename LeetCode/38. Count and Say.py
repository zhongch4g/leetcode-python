#-*-coding:utf-8 -*-
"""
    38. Count and Say
    Directed by user zhongch4g
    current system date 2017/5/11
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # It seems not only me misunderstood the question.
        # Please modify the description, since it's frustrating if you are solving a "different" question.
        # 需要得到n的排列
        # 1, 11, 21, 1211, 111221, 312211， ...
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
