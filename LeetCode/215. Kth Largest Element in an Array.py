#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 4:06 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 215. Kth Largest Element in an Array.py
# @Software: IntelliJ IDEA

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


    def partition(self, nums, left, right):
        pivot = nums[right]
        cur = left - 1
        for i in range(left, right):
            if nums[i] <= pivot:
                cur += 1
                nums[cur], nums[i] = nums[i], nums[cur]
        nums[cur + 1], nums[right] = nums[right], nums[cur + 1]
        print(nums)
        print("index: ", cur + 1)
        return cur + 1

    # 第k小
    def minik(self, array, k):
        m = 0
        n = len(array)-1
        index = self.partition(array, m, n)
        while index != k-1:
            if index > k-1:
                index = self.partition(array, m, index-1)
            if index < k-1:
                index = self.partition(array, index+1, n)

        print(array)
        print(array[k-1])

    def partition_topk(self, nums, left, right):
        pivot = nums[right]
        cur = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        nums[cur], nums[right] = nums[right], nums[cur]
        print(nums)
        print("index: ", cur)
        return cur

    def topk(self, array, k):
        m = 0
        n = len(array)-1
        index = self.partition_topk(array, m, n)
        while index != k-1:
            if index > k-1:
                index = self.partition_topk(array, m, index-1)
            if index < k-1:
                index = self.partition_topk(array, index+1, n)

        print(array)
        print(array[k-1])

    def recurtopk(self, array, m, n, k):
        if m == n:
            return array[m]
        pivot = self.partition(array, m, n)
        i = pivot-m+1
        print(pivot, i, k,array)
        if i == k:
            return array[pivot]
        elif i > k:
            return self.recurtopk(array, m, pivot-1, k)
        else:
            return self.recurtopk(array, pivot+1, n, k-i)



nums = [3,2,3,1,2,4,5,5,6]
solution = Solution()
solution.topk([3,2,3,1,8,9,10,5,6], 2)
# res = solution.recurtopk([3,2,3,1,8,9,10,5,6], 0, len(nums), 2)
# print(res)
