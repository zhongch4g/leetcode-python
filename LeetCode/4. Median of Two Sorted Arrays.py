#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 9:16 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 4. Median of Two Sorted Arrays.py
# @Software: IntelliJ IDEA


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = len(nums1) + len(nums2)
        if k % 2:
            return self.findKth(nums1, nums2, k // 2 + 1)
        else:
            smaller = self.findKth(nums1, nums2, k // 2)
            bigger = self.findKth(nums1, nums2, k // 2 + 1)
            return (smaller + bigger) / 2


    def findKth(self, A, B, k):
        i, j = 0, 0

        while(1):
            if len(A) == i:
                return B[j + k - 1]
            if len(B) == j:
                return A[i + k - 1]
            if k == 1:
                break

            cut = k // 2
            a = A[i + cut - 1] if i + cut <= len(A) else None
            b = B[j + cut - 1] if j + cut <= len(B) else None
            if b is None or (a is not None and a < b):
                i += cut
            else:
                j += cut
            k -= cut

        return min(A[i], B[j])


    def findMedianSortedArraysRecur(self, nums1, nums2):
        k = len(nums1) + len(nums2)
        if k % 2:
            return self.findKth2(nums1, 0, nums2, 0, k // 2 + 1)
        else:
            smaller = self.findKth2(nums1, 0, nums2, 0, k // 2)
            bigger = self.findKth2(nums1, 0, nums2, 0, k // 2 + 1)
            return (smaller + bigger) / 2


    def findKth2(self, A, i, B, j, k):
        if i == len(A):
            return B[j + k - 1]
        if j == len(B):
            return A[i + k - 1]
        if k == 1:
            return min(A[i], B[j])

        a = A[i + k // 2 - 1] if i + k // 2 <= len(A) else None
        b = B[j + k // 2 - 1] if j + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.findKth2(A, i + k // 2, B, j, k - k // 2)
        return self.findKth2(A, i, B + k // 2, j, k - k // 2)



nums1 = [1, 2]
nums2 = [3, 4, 5]

solution = Solution()
res = solution.findMedianSortedArraysRecur(nums1, nums2)
print(res)

