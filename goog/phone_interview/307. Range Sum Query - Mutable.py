#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 4:43 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 307. Range Sum Query - Mutable.py
# @Software: IntelliJ IDEA


"""
用了prefix sum，每次更新数组之后，同时更新prefix sum数组
更新操作最差O(n)
结果超时了

看了解答 貌似需要用到segment tree
segment tree two operations
1. compute the minimum of a range
2. update a value

suppose
[1, 5, 3, 7, 3, 2, 5, 7]
minimum in range (1, 7) is 2
now update value at index 5 to the value 6
minimum in range (3, 8) is 3

demands :
1. fast computation of minima O(n) --> O(logn)
2. fast updating of values O(1) --> O(logn)


youtube link: https://youtu.be/Oq2E2yGadnU
"""

class NumArray:

    def __init__(self, nums):
        self.data = [0 for _ in nums] + nums
        self.n = len(nums)

        for idx in reversed(range(1, self.n)):
            self.data[idx] = self.data[2*idx] + self.data[2*idx + 1]

    def update(self, i: int, val: int) -> None:
        idx = i + self.n
        self.data[idx] = val
        while idx > 1:
            idx //= 2
            self.data[idx] = self.data[2*idx] + self.data[2*idx + 1]


    def sumRange(self, i: int, j: int) -> int:
        #sum [i,j] = sum [i, j)
        left = i + self.n
        right = j + self.n +1
        sum_range = 0
        while left < right:
            if left%2:
                sum_range += self.data[left]
                left +=1
            if right %2:
                right -= 1
                sum_range += self.data[right]
            left //= 2
            right //= 2

        return sum_range