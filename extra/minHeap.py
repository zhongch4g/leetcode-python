#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 9:18 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : minHeap.py
# @Software: IntelliJ IDEA

class minimumHeap(object):
    def __init__(self, arr, heapsize):
        self.arr = arr
        self.heapsize = heapsize

    def minHeapify(self, arr, i):

        smallest = i

        if 2*i <= self.heapsize and arr[i] > arr[2*i]:
            smallest = 2*i
        else:
            smallest = i
        if 2*i + 1 <= self.heapsize and arr[2*i +1] < arr[smallest]:
            smallest = 2*i + 1

        if i != smallest:
            # swap
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(arr, smallest)

    def minHeap(self, arr):
        # 最后一个非叶结点开始遍历
        for i in range(len(arr)//2, 0, -1):
            self.minHeapify(arr, i)
        print(arr)

    def heapSort(self, arr):
        for i in range(len(arr) - 1, 1, -1):
            arr[1], arr[i] = arr[i], arr[1]
            self.heapsize -= 1
            self.minHeapify(arr, 1)

    def run(self):
        self.minHeap(self.arr)
        self.heapSort(arr)
        print(self.arr)


arr = [-1, 4, 5, 1, 6, 2, 7, 3, 8]
minimumHeap = minimumHeap(arr, len(arr) - 1)
minimumHeap.run()
