#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 8:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : swapped_number_in_sorted_list.py
# @Software: IntelliJ IDEA



def find_two_swapped(nums) -> (int, int):
    n = len(nums)
    x = y = -1
    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            y = nums[i + 1]
            # first swap occurence
            if x == -1:
                x = nums[i]
            # second swap occurence
            else:
                break
    return x, y


find_two_swapped([1, 2, 8, 4, 5, 6, 7, 3, 9])