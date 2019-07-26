#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 12:50 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : quick_sort.py
# @Software: IntelliJ IDEA


class Solution:
    def sortIntegers2(self, A):
        # Write your code here
        self.quickSort(A, 0, len(A) - 1)
        print(A)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        # key point 1: pivot is the value, not the index
        pivot = A[(start + end) // 2]

        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]

                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)