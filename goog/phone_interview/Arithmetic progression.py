#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 3:17 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : Arithmetic progression.py
# @Software: IntelliJ IDEA

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.longest = 1

    def longest_ap_in_bt(self ,root):
        if not root:
            return 0
        self.search(root, None, 1)
        print(self.longest)
        return self.longest

    def search(self, root, diff, cur_len):

        if root.left:
            d = root.val - root.left.val
            if not diff:
                diff = d
                self.search(root.left, diff, cur_len + 1)
            else:
                if d == diff:
                    self.longest = max(self.longest, cur_len + 1)
                    self.search(root.left, diff, cur_len + 1)

        if root.right:
            d = root.val - root.right.val
            if not diff:
                diff = d
                self.search(root.right, diff, cur_len + 1)
            else:
                if d == diff:
                    self.longest = max(self.longest, cur_len + 1)
                    self.search(root.right, diff, cur_len + 1)




node1 = Node(2)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)
node5 = Node(7)
node6 = Node(0)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
solution = Solution()
solution.longest_ap_in_bt(node1)