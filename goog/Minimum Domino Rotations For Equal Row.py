#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 12:58 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : Minimum Domino Rotations For Equal Row.py
# @Software: IntelliJ IDEA


import sys
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        minimum = sys.maxsize
        for i in range(1, 7):
            minimum = min(minimum, self.number_of_rotate(A, B, i))
            minimum = min(minimum, self.number_of_rotate(B, A, i))
        return minimum if minimum != sys.maxsize else -1

    def number_of_rotate(self, A, B, n):
        count = 0
        for i in range(len(A)):
            if A[i] == n:
                continue

            if B[i] == n:
                count += 1
            else:
                return sys.maxsize
        return count

import sys
class Solution2(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        minimum = sys.maxsize
        minimum = min(minimum, self.number_of_rotate(A, B, A[0]))
        minimum = min(minimum, self.number_of_rotate(A, B, B[0]))
        return minimum if minimum != sys.maxsize else -1

    def number_of_rotate(self, A, B, n):
        count_a = 0
        count_b = 0
        for i in range(len(A)):
            if A[i] != n and B[i] != n:
                return sys.maxsize
            elif A[i] != n:
                count_a += 1
            elif B[i] != n:
                count_b += 1
        return min(count_a, count_b)


def minDominoRotations(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    minimum = sys.maxsize
    for i in range(1, 7):
        minimum = min(minimum, number_of_rotate(A, B, i))
        minimum = min(minimum, number_of_rotate(B, A, i))
    return minimum if minimum != sys.maxsize else -1

def number_of_rotate(A, B, n):
    count = 0
    for i in range(len(A)):
        if A[i] == n:
            continue

        if B[i] == n:
            count += 1
        else:
            return sys.maxsize
    return count


solution = Solution2()
solution.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2])