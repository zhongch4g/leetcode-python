#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 8:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 629. Minimum Spanning Tree.py
# @Software: IntelliJ IDEA



class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

import functools

def comp(a, b):
    if a.cost != b.cost:
        return a.cost - b.cost

    if a.city1 != b.city1:
        if a.city1 < b.city1:
            return -1
        else:
            return 1

    if a.city2 == b.city2:
        return 0
    elif a.city2 < b.city2:
        return -1
    else:
        return 1

class Solution:
    # @param {Connection[]} connections given a list of connections include two cities and cost
    # @return {Connection[]} a list of connections from results
    def print(self, conn):
        for i in conn:
            print(i.city1, i.city2, i.cost)


    def lowestCost(self, connections):
        # Write your code here
        # 按照两个城市的距离 和 城市的字典序给connections排序 从小到大
        connections.sort(key=functools.cmp_to_key(comp))
        self.print(connections)
        hash = {}
        n = 0
        for connection in connections:
            if connection.city1 not in hash:
                n += 1
                hash[connection.city1] = n

            if connection.city2 not in hash:
                n += 1
                hash[connection.city2] = n
        # 构造father数组 n == number of city 从1开始
        father = [0 for _ in range(n + 1)]

        results = []
        for connection in connections:
            num1 = hash[connection.city1]
            num2 = hash[connection.city2]

            root1 = self.find(num1, father)
            root2 = self.find(num2, father)
            # 这一步要注意 是判断加了这一条线 会不会变成环的 如果两个点的父节点是相同的那么就是有环
            if root1 != root2:
                father[root1] = root2
                results.append(connection)

        if len(results)!= n - 1:
            return []
        return results

    def find(self, num, father):
        # when its root is 0 return itself
        if father[num] == 0:
            return num
        father[num] = self.find(father[num], father)
        return father[num]


c1 = Connection("Acity","Bcity",1)
c2 = Connection("Acity","Ccity",2)
c3 = Connection("Bcity","Ccity",3)
solution = Solution()
res = solution.lowestCost([c1, c2, c3])
for i in res:
    print(i.city1, i.city2, i.cost)

