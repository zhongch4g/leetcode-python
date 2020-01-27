#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 12:41 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : LIRS.py
# @Software: IntelliJ IDEA

import collections
import itertools

class LirsCache(object):

    def __init__(self, s_capacity, q_capacity):
        self.s_capacity = s_capacity
        self.q_capacity = q_capacity
        self.cache = dict()
        self.s = collections.OrderedDict()
        self.q = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            if len(self.s) < self.s_capacity:
                # miss, we have space
                self.s[key] = key
                self.cache[key] = key
            elif key not in self.s:
                # miss, new value o long time no see
                # x = self.q.popitem(False)[0]
                # self.cache.pop(x)
                self.s[key] = key
                self.q[key] = key
                self.cache[key] = key
            elif key in self.s:
                # miss, with HIR non resident
                x = self.q.popitem(False)[0]
                self.cache.pop(x)
                self.s[key] = key
                y = self.s.popitem(False)[0]
                self.q[y] = y
                self.prune()
            else:
                assert False
        else:
            if key in self.s and key not in self.q:
                # hit LIR
                x = self.s.pop(key)
                self.s[key] = key
                self.prune()
            elif key in self.s and key in self.q:
                # hit HIR
                x = self.s.pop(key)
                self.s[key] = key
                self.q.pop(key)
                x = self.s.popitem(False)[0]
                self.q[x] = x
                self.prune()
            elif key not in self.s and key in self.q:
                # hit old HIR
                self.s[key] = key
                self.q.pop(key)
                self.q[key] = key
            else:
                assert False

    def prune(self):
        while self.s:
            oldest = list(self.s.keys())[0]
            print(oldest)
            if oldest not in self.q and oldest in self.cache:
                # oldest is LIR
                return
            oldest = self.s.popitem(False)
            if oldest in self.q:
                self.q.pop(oldest)
            print("---")


lirs = LirsCache(2, 1)
lirs.get('A')
lirs.get('D')
lirs.get('B')
lirs.get('C')
lirs.get('B')
lirs.get('A')
lirs.get('D')
lirs.get('A')
lirs.get('E')
print(lirs.s)
print("----------")
print(lirs.q)

