#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 11:46 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 981. Time Based Key-Value Store.py
# @Software: IntelliJ IDEA

import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_ts = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_ts[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        all_values = self.key_to_ts.get(key, None)
        if not all_values: return ""
        i = self.binary_search(all_values, timestamp)
        return all_values[i][1] if i is not None else ""

    def binary_search(self, values, timestamp: int):
        i, j = 0, len(values) - 1
        # contain only one element

        while i + 1 < j:
            mid = (i + j) // 2
            if values[mid][0] < timestamp:
                i = mid
            else:
                j = mid
        if values[j][0] <= timestamp:
            return j
        if values[i][0] <= timestamp:
            return i
        return None



        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)