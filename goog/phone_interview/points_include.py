#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 4:23 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : points_include.py
# @Software: IntelliJ IDEA


"""
给一堆点(non-negative坐标，不会有(0,0)，不会有两个点的连线过原点)，对于(x1,y1)，
构成(0, 0) (x1, 0)的直角三角形，求几个点被包含在这个三角形中。
要‍‍‌‌‍‌‌‌‌‍‍‍‌‍‍‌‍‌‍求对每一个点都构成这样的三角形，求有几个点被包含。
"""

"""
方法一：固定一个点，遍历其他点，满足如下两个条件即包含
1、y-kx < 0 
2、x_i < x_cur
复杂度O(n^2)

还有一种想法 按x从小到大排序 这样只需要比较斜率 但是这样复杂度貌似更高 没想到怎么组织
"""