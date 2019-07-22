#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 7:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : heap.py
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
        largest = -99999
        if l <= self.heapsize and arr[i] < arr[l]:
            largest = l
        else:
            largest = i

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

    def heapsort(self, arr):
        self.buildMaxheap(arr)
        for i in range(len(arr)-1, 1, -1):
            arr[1], arr[i] = arr[i], arr[1]
            self.heapsize -= 1
            self.maxHeapify(arr, 1)

    def run(self):
        self.heapsort(self.arr)
        return self.arr[1:]

arr = [-1, 4, 5, 1, 6, 2, 7, 3, 8]
heap = heap(arr, len(arr) - 1)
sortedarr = heap.run()
print(sortedarr)
