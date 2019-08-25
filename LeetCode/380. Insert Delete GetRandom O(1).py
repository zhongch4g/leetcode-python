#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 5:47 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 380. Insert Delete GetRandom O(1).py
# @Software: IntelliJ IDEA


import random
class RandomizedSet:

    """
    random : list
    insert remove: hash
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomizedset = []
        self.hash = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash:
            return False

        self.randomizedset.append(val)
        self.hash[val] = len(self.randomizedset) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash:
            return False

        # index from set
        index = self.hash[val]

        self.hash[self.randomizedset[-1]] = index

        self.hash.pop(val, None)


        self.randomizedset[index], self.randomizedset[-1] = self.randomizedset[-1], self.randomizedset[index]

        self.randomizedset.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.randomizedset:
            return -1

        i = random.randint(0, len(self.randomizedset) - 1)
        return self.randomizedset[i]


        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()