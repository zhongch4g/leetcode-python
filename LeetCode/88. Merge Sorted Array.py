#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 6:41 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 88. Merge Sorted Array.py
# @Software: IntelliJ IDEA


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1

        while index1 >= 0:
            nums1[index] = nums1[index1]
            index -= 1
            index1 -= 1
        while index2 >= 0:
            nums1[index] = nums2[index2]
            index -= 1
            index2 -= 1
        return nums1