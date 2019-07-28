#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:23 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 491. Palindrome Number.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):

        rev = 0
        temp = num
        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10
        if rev == num:
            return True
        return False
