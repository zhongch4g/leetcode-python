#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 9:02 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : binaryTreePath.py
# @Software: IntelliJ IDEA


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        # Solve
        if (root is None):
            return []

        if (root.left is None and root.right is None):
            return [str(root.val)]
        paths = []

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        # Combine
        for path in left:
            paths.append(str(root.val) + '->' + path)
        for path in right:
            paths.append(str(root.val) + '->' + path)
        return paths

    def traverse_binary_tree_path(self, root):
        if (root is None):
            return []
        path = []
        self.dfs(root, [str(root.val)], path)
        print(path)

    def dfs(self, root, curpath, path):
        if (root.left is None and root.right is None):
            path.append('->'.join(curpath))
            return

        if (root.left):
            curpath.append(str(root.left.val))
            self.dfs(root.left, curpath, path)
            curpath.pop()
        if (root.right):
            curpath.append(str(root.right.val))
            self.dfs(root.right, curpath, path)
            curpath.pop()


    def maximum_depth_of_binary_tree(self, root):
        if (root is None):
            return 0
        if (root.left is None and root.right is None):
            return 1

        left = self.maximum_depth_of_binary_tree(root.left)
        right = self.maximum_depth_of_binary_tree(root.right)

        # Solve
        return max(left, right) + 1



root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
solution = Solution()
print(solution.traverse_binary_tree_path(root))
# print(solution.maximum_depth_of_binary_tree(root))