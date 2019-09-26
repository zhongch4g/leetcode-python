#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 11:40 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : watering_tree.py
# @Software: IntelliJ IDEA

class tree_node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.to_left_cost = 0
        self.to_right_cost = 0


class Solution:
    def time_cost(self, root):
        self.all_cost = 0
        self.search(root, 0)
        return self.all_cost

    def search(self, root, cur_sum):
        if not root.left and not root.right:
            self.all_cost += cur_sum
        if root.left:
            self.search(root.left, cur_sum + root.to_left_cost)
        if root.right:
            self.search(root.right, cur_sum + root.to_right_cost)


root = tree_node(0)
root.to_left_cost = 1
root.to_right_cost = 2
root1 = tree_node(1)
root1.to_left_cost = 3
root1.to_right_cost = 4
root2 = tree_node(2)
root3 = tree_node(3)
root4 = tree_node(4)

root.left = root1
root.right = root2
root1.left = root3
root1.right = root4


solution = Solution()
res = solution.time_cost(root)
print(res)