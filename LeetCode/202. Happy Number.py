#-*-coding:utf-8 -*-
"""
    202. Happy Number
    Directed by user zhongch4g
    current system date 2017/4/27
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        remember = set()

        while n != 1 and n not in remember:
            remember.add(n)

            n = self.get_next(n)

        if n == 1:
            return True
        return False


    def get_next(self, n):
        square_sum = 0
        while n:
            k = n % 10
            square_sum += k ** 2
            n //= 10
        return square_sum
