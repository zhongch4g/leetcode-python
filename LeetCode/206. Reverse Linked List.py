#-*-coding:utf-8 -*-
"""
    206. Reverse Linked List
    Directed by user zhongch4g
    current system date 2017/4/23
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # list = []
        # temp = head
        # if head is None:
        #     return list
        # while temp.next is not None:
        #     list.append(temp.val)
        #     temp = temp.next
        # list1 = list.reverse()
        # i = 0
        # while head.next is not None:
        #     head.val = list1[i]
        #     i += 1
        # return head

