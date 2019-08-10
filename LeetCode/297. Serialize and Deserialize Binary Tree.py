#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 12:16 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 297. Serialize and Deserialize Binary Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if (not root):
            return ""

        queue = collections.deque([root])
        serialize_list = []
        while (queue):
            node = queue.popleft()
            # current node
            serialize_list.append(str(node.val) if node else "#")
            if (node):
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(serialize_list)


    def deserialize(self, data):
        # write your code here
        if (not data):
            return None
        order = [TreeNode(int(val)) if val != "#" else None for val in data.split()]

        root = order[0]
        idx = 0
        idx2 = 1
        nodes = [root]
        while (idx < len(nodes)):
            node = nodes[idx]
            idx += 1
            node.left = order[idx2]
            node.right = order[idx2 + 1]
            idx2 += 2

            if (node.left):
                nodes.append(node.left)
            if (node.right):
                nodes.append(node.right)
        return root




        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))