#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 2:18 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_sorted_array.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    # 从后往前加入数据，大的数据放最后
    def mergeSortedArray(self, A, m, B, n):
        index = m + n - 1
        index1, index2 = m - 1, n - 1
        while index1 >= 0 and index2 >= 0:
            if A[index1] > B[index2]:
                A[index] = A[index1]
                index -= 1
                index1 -= 1
            else:
                A[index] = B[index2]
                index -= 1
                index2 -= 1

        while index1 >= 0:
            A[index] = A[index1]
            index -= 1
            index1 -= 1
        while index2 >= 0:
            A[index] = B[index2]
            index -= 1
            index2 -= 1
