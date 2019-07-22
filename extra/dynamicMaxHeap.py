#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 10:17 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : dynamicMaxHeap.py
# @Software: IntelliJ IDEA

class heap(object):
    def __init__(self, arr, heapsize):
        self.arr = arr
        self.heapsize = heapsize

    # O(logn) = O(h)
    def maxHeapify(self, arr, i):
        # left node
        l = i * 2
        # right node
        r = i * 2 + 1
        largest = i
        if l <= self.heapsize and arr[i] < arr[l]:
            largest = l

        if r <= self.heapsize and arr[largest] < arr[r]:
            largest = r

        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(arr, largest)

    def buildMaxheap(self, arr):
        heapsize = len(arr) - 1
        # from heapsize//2 downto 1
        for i in range(self.heapsize//2, 0, -1):
            self.maxHeapify(arr, i)

    # dynamic insert
    def minimumK(self, arr, k):
        result = [-1]
        for i in range(1, len(arr)):
            if self.heapsize != k:
                result.append(arr[i])
                self.heapsize += 1
                self.buildMaxheap(result)
            else:
                if arr[i] < result[1]:
                    result.pop(1)
                    self.heapsize -= 1
                    result.append(arr[i])
                    self.buildMaxheap(result)
        return result[1:]

    def run(self):
        return self.minimumK(self.arr, 4)

arr = [-1, 4, 5, 1, 6, 2, 7, 3, 8]
heap = heap(arr, 0)
sortedarr = heap.run()
print(sortedarr)