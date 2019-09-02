#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 7:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 295. Find Median from Data Stream.py
# @Software: IntelliJ IDEA


import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.count_elem = 0

    def addNum(self, num: int) -> None:

        # convert pos to neg or neg to pos
        heapq.heappush(self.max_heap, - num)
        if self.count_elem % 2 == 0:
            if not self.min_heap:
                self.count_elem += 1
                return
            else:
                if - self.max_heap[0] > self.min_heap[0]:
                    max_root = - heapq.heappop(self.max_heap)
                    min_root = heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, - min_root)
                    heapq.heappush(self.min_heap, max_root)
        else:
            heapq.heappush(self.min_heap, - heapq.heappop(self.max_heap))
        self.count_elem += 1

    def findMedian(self) -> float:
        if self.count_elem % 2 == 1:
            return - self.max_heap[0]
        else:
            if self.count_elem == 0:
                return
            return (- self.max_heap[0] + self.min_heap[0]) / 2


            # Your MedianFinder object will be instantiated and called as such:
            # obj = MedianFinder()
            # obj.addNum(num)
            # param_2 = obj.findMedian()