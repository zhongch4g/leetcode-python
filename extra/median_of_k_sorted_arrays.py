#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 7:08 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : median_of_k_sorted_arrays.py
# @Software: IntelliJ IDEA

"""
1. find range of all list number,
start = min(all the lists' first number), end = max(all the lists' last number)
2. find the mid number in this range,
use binary search to find how many number is smaller than this mid number
in each list
3. the time complexity of this algorithm is log(R)*k*log(n)
"""
