#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 2:21 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : backspace.py
# @Software: IntelliJ IDEA


"""
给两个char array，其中有一些char为backspace就是删除前面的字符，
要求输出一个boolean判断两个char array是否相同，时间要求O(n) , 空间要求O(1)
例如：
[a,b,'\b',d,c] 和[a,d,c] true
[a,b,'\b','\b','\b',d,c] 和 [d,c] true
[a,b,d,'\b'] 和 [a,d] false

用Stack的方法，TimeO(n), SpaceO(‍‍‌‌‍‌‌‌‌‍‍‍‌‍‍‌‍‌‍n)
要求TimeO(n), SpaceO(1)，从后往前parse
"""

class Solution:
    def is_same_array(self, arr1, arr2):

        backspace = 0

        for i in range(len(arr1) - 1, -1, -1):
            if arr1[i] == '\b':
                backspace += 1
                arr1[i] = False
            elif backspace > 0:
                backspace -= 1
                arr1[i] = False

        j = 0
        for i in range(len(arr1)):
            if not arr1[i]:
                continue
            if arr1[i] and arr1[i] == arr2[j]:
                j += 1
                continue
            return False
        if len(arr2) == j:
            return True
        return False


arr1 = ['a','b','\b','d','c']
arr2 = ['a','d','c']
arr3 = ['a','b','\b','\b','\b','d','c']
arr4 = ['d','c']
solution = Solution()
res = solution.is_same_array(arr3, arr4)
print(res)