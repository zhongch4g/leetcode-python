#-*-coding:utf-8 -*-
"""
    237. Delete Node in a Linked List
    Directed by user zhongch4g
    current system date 2017/4/19
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 理解错题目的意思，以为是传入链表
        # if node.next is not None:
        #     pre = None
        #     for i in self:
        #         if i is node and pre is None:
        #             i.next = None
        #         if i is node and pre is not None:
        #             pre.next = i.next
        #         pre = i
        #         i = i.next
        # 仅仅是移除了节点，但是没有真正删除
        node.val = node.next.val
        node.next = node.next.next