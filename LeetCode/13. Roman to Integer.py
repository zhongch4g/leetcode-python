#-*-coding:utf-8 -*-
"""
    13. Roman to Integer
    Directed by user zhongch4g
    current system date 2017/4/22
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

        prev_val = total =0

        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_val:
                total -= int_val
            else:
                total += int_val
            prev_val = int_val

        return total

instance = Solution()
print instance.romanToInt("DCXXI")
s = "DCXXI"
print range(len(s) - 1, -1, -1)