#-*-coding:utf-8 -*-
"""
    83. Remove Duplicates from Sorted List
    Directed by user zhongch4g
    current system date 2017/5/1
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        index0 = head
        index = head.next
        while index is not None:
            if index0.val == index.val:
                index = index.next
            else:
                index0.next = index
                index0 = index0.next
                index = index.next
        index0.next = index
        return head

#[-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34]