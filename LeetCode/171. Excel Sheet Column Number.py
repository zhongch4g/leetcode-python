#-*-coding:utf-8 -*-
"""
    171. Excel Sheet Column Number
    Directed by user zhongch4g
    current system date 2017/4/18
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
                'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        col = 0
        length = len(s)
        temp = length
        for i in s:
            col = col + dict[i] * (26 ** (temp - 1))
            temp = temp - 1
        return col

    # ord(char) 会返回char的ascii码值
    def solution_1(self, s):
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

instance = Solution()
print instance.titleToNumber("AAA")
print instance.solution_1("ZZ")

list1 = [ord(c) - 64 for c in list("AB")]
