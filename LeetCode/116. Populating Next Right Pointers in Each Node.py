#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 4:07 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 116. Populating Next Right Pointers in Each Node.py
# @Software: IntelliJ IDEA



# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            nxt = None
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                if not nxt:
                    nxt = curr
                    continue
                nxt.next = curr
                nxt = curr
        return root
