#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 5:12 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 347. Top K Frequent Elements.py
# @Software: IntelliJ IDEA


import heapq, collections
class Solution:
    def topKFrequent(self, nums, k: int):
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1

        heap = []
        # min heap
        for key, v in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key))
            else:
                if v > heap[0][0]:
                    heapq.heapreplace(heap, (v, key))
                    # print(heap)
        return [v for key, v in heap]

class Solution1:
    def topKFrequent(self, nums, k):
        frq = collections.defaultdict(list)
        for key, cnt in collections.Counter(nums).items():
            frq[cnt].append(key)
        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]