#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 3:46 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : median_of_two_sorted_array.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findkth(A, B, n // 2 + 1)
        else:
            smaller = self.findkth(A, B, n // 2)
            bigger = self.findkth(A, B, n // 2 + 1)
            return (smaller + bigger) / 2

    def findkth(self, A, B, k):
        i, j = 0, 0
        while 1:
            if len(A) == i:
                return B[j + k - 1]
            if len(B) == j:
                return A[i + k - 1]
            if k == 1:
                break

            cut_len = k // 2

            a = A[i + cut_len - 1] if i + cut_len <= len(A) else None
            b = B[j + cut_len - 1] if j + cut_len <= len(B) else None

            if b is None or (a is not None and a < b):
                i += cut_len
            else:
                j += cut_len

            k -= cut_len

        return min(A[i], B[j])


# A = [2, 4, 6, 8]
# B = [1, 3, 5, 7]
A = [1]
B = [2]
solution = Solution()
result = solution.findMedianSortedArrays(A, B)
print(result)



