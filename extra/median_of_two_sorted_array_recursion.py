#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 4:43 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : median_of_two_sorted_array_recursion.py
# @Software: IntelliJ IDEA
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        # 求奇偶两种情况，通过寻找固定的第k个数
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        # 其中一个到头了，那么就将k加到另一个list
        if len(A) == index_a:
            return B[index_b + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        # 如果k==1，则返回两个中更小的
        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None

        # 判断b是None代表b是无穷大，这个时候直接在list A中减去k//2个数
        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)


A = [2]
B = [1]
solution = Solution()
result = solution.findMedianSortedArrays(A, B)
print(result)