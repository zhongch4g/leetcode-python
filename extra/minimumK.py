#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 4:27 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : minimumK.py
# @Software: IntelliJ IDEA

class Solution:
    def GetLeastNumbers_Solution1(self, tinput, k):
        # write code here
        # solution1 : 排序后取前k个
        # self.quicksort(tinput, 0, len(tinput) - 1)
        # return tinput[:4]
        l=[-1,26,5,77,1,61,11,59,15,48,19] #第一个元素不用，占位
        res=self.heapSort(l)
        # print(res)

    def partition1(self, arr, p, q):
        i = p - 1
        key = arr[q]
        for j in range(p, q):
            if arr[j] <= key:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[q] = arr[q], arr[i + 1]
        return i + 1

    def quicksort1(self, inpt, i, j):
        if i < j:
            idx = self.partition(inpt, i, j)
            self.quicksort(inpt, i, idx - 1)
            self.quicksort(inpt, idx + 1, j)

    def fixDown1(self, a,k,n): #自顶向下堆化，从k开始堆化
        N=n-1
        while 2*k<=N:
            j=2*k
            if j<N and a[j]<a[j+1]: #选出左右孩子节点中更大的那个
                j+=1
            if a[k]<a[j]:
                a[k],a[j]=a[j],a[k]
                k=j
            else:
                break

    def heapSort1(self,l):
        n=len(l)-1
        for i in range(n//2,0,-1):
            self.fixDown(l,i,len(l))
        while n>1:
            l[1],l[n]=l[n],l[1]
            self.fixDown(l,1,n)
            n-=1
        return l[1:]


    #######################################
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # solution 3 小顶堆
        if k > len(tinput):
            return []
        node = [-1]
        tinput = node + tinput
        heapsize = len(tinput) - 1
        # 存储在最小堆
        heapsize, tinput = self.minHeap(tinput, heapsize)
        num = self.heapSort(tinput, k, heapsize)
        return num

    def minHeapify(self, arr, i, heapsize):
        smallest = i
        if 2*i <= heapsize and arr[i] > arr[2*i]:
            smallest = 2*i
        else:
            smallest = i
        if 2*i + 1 <= heapsize and arr[2*i + 1] < arr[smallest]:
            smallest = 2*i + 1
        if i != smallest:
            # swap
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(arr, smallest, heapsize)

    def minHeap(self, arr, heapsize):
        # 最后一个非叶结点开始遍历
        for i in range(len(arr)//2, 0, -1):
            self.minHeapify(arr, i, heapsize)
        return heapsize, arr

    def heapSort(self, arr, k, heapsize):
        for i in range(len(arr) - 1, len(arr) - 1 - k, -1):
            arr[1], arr[i] = arr[i], arr[1]
            heapsize -= 1
            self.minHeapify(arr, 1, heapsize)
        return arr[:-k-1:-1]





solution = Solution()
minimum = solution.GetLeastNumbers_Solution([4, 5, 6, 2, 7, 3, 8], 4)
print(minimum)