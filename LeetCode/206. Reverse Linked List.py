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

        # 反转单链表(O(N) 空间复杂度)
        nodeList = []
        if head is None:
            return None
        while head is not None:
            nodeList.append(head.val)
            head = head.next
        nodeList.reverse()
        newHead = ListNode(nodeList[0])
        rhead = newHead
        for val in nodeList[1:]:
            node = ListNode(val)
            newHead.next = node
            newHead = newHead.next
        return rhead

    def reverseList1(self, head):
        cur = head
        nex = head
        pre = None
        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        p, q = head, head.next
        while q:
            temp = q.next
            q.next = p
            p, q = q, temp

        head.next = None

        return p


    def reverseList4(self, head):
        cur = head
        nex = head
        pre = None
        while cur is not None:
            nex = cur.next
            cur.next = pre

            pre = cur
            cur = nex
        return pre
