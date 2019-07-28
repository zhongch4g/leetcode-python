#-*-coding:utf-8 -*-
"""
    234. Palindrome Linked List
    Directed by user zhongch4g
    current system date 2017/5/21
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Follow up:
Could you do it in O(n) time and O(1) space?
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 确定长度
        n = 0
        trav = head
        while trav:
            n += 1
            trav = trav.next

        # 先翻转一半
        n = n // 2 if n & 1 else n // 2 - 1
        dummy = head
        for i in range(n):
            dummy = dummy.next
        cur = dummy.next
        dummy.next = None
        ###### 找中间值这里可以优化，是有快慢指针，慢指针一次走一步 快指针一次走两步


        while cur:
            temp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = temp
        dummy = dummy.next
        while dummy:
            if head.val != dummy.val:
                return False
            head = head.next
            dummy = dummy.next
        return True



# 1->9->8->7->8->9->1
# 1->9->8->8->9->1
node1 = ListNode(0)
node2 = ListNode(0)
node1.next = node2
instance = Solution()
print (instance.isPalindrome(node1))