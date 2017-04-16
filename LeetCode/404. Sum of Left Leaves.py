#-*-coding:utf-8 -*-
"""
    404. Sum of Left Leaves
    Directed by user zhongch4g
    current system date 2017/4/16
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # 确定该节点为左叶子，即左边节点没有子节点
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    # dfs解决方案
    # def sumOfLeftLeaves(self, root):
    #     def dfs(root, left):
    #         if not root: return
    #         if left and not root.left and not root.right:
    #             cache[0] += root.val
    #         dfs(root.left,  True)
    #         dfs(root.right, False)
    #
    #     cache = [0]
    #     dfs(root, False)
    #     return cache[0]
