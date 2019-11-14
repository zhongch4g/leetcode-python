#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 9:30 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : calc_ignore.py
# @Software: IntelliJ IDEA

class CalcIgnore:
    def calulate(self, value_list):
        base = 1
        for val in value_list:
            base = base * (1 - val * 0.01)
        return 1 - base


# main = [20]  link = [15]  super = [18]
base = [68]
main = [20]
assistant = [30, 30]
combo = [15]

lack = [30]

value_list = base + main + assistant + combo + lack
obj = CalcIgnore()
res = obj.calulate(value_list)
print(res)