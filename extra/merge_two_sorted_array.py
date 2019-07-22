#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 2:11 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_two_sorted_array.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        index1, index2 = 0, 0
        C = []
        while index1 < len(A) and index2 < len(B):
            if A[index1] < B[index2]:
                C.append(A[index1])
                index1 += 1
            else:
                C.append(B[index2])
                index2 += 1
        while index1 < len(A):
            C.append(A[index1])
            index1 += 1
        while index2 < len(B):
            C.append(B[index2])
            index2 += 1
        return C


A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
solution = Solution()
C = solution.mergeSortedArray(A, B)
print(C)