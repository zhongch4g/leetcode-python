#-*-coding:utf-8 -*-
"""
    374. Guess Number Higher or Lower
    Directed by user zhongch4g
    current system date 2017/5/10
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # def binary(num, first, end):
        #     if guess(num) == 0:
        #         return num
        #     elif guess(num) == -1:
        #         binary((num + end) / 2, num + 1, end)
        #     elif guess(num) == 1:
        #         binary((first + num) / 2, first, num - 1)
        #
        # first = 0
        # end = n
        # return binary((first + end) / 2, first, end)

        # pick number from 1 to n
        left = 1
        right = n
        while left <= right:
            mid = (right - left) / 2 +  left
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                left = mid + 1
            else:
                right = mid - 1

        # 递归版本
    def guessNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(1,n)

    def binary_search(self, min, max):
        mid = (min + max) / 2
        k = guess(mid)
        if k == 0:
            return mid
        elif k > 0:
            return self.binary_search(mid + 1, max)
        else:
            return self.binary_search(min, mid - 1)