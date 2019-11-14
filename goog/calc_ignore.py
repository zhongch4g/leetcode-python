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

base = [68]
main = [20]
assistant = [30, 30]
link = [15]
combo = [15]
super = [18]
value_list = base + main + assistant + link + combo + super
obj = CalcIgnore()
res = obj.calulate(value_list)
print(res)