#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 9:15 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 22. Generate Parentheses.py
# @Software: IntelliJ IDEA


class Solution:
    def generateParenthesis(self, n):
        results = []
        if n == 0:
            return []
        self.search(n, n-1, '(', results)
        return results

    def search(self, n, index, result, results):

        if index == 0 and len(result) == 2*n and self.isValid(result):
            results.append(result)
            return

        if len(result) > 2*n:
            return

        if index != 0:
            self.search(n, index-1, result + '(', results)

        self.search(n, index, result + ')', results)



    def isValid(self, parentheses):
        stack = []
        d = {'(': ')'}
        for c in parentheses:
            if c == '(':
                stack.append(c)
            elif stack and d[stack.pop()] == c:
                continue
            else:
                return False

        return stack == []


    # 搜索版本
    def generateParenthesis2(self, n):
        basket = []
        self.generate2(n,n,"",basket)
        return basket

    def generate2(self,left,right,single,basket):
        if left > 0:
            self.generate2(left-1, right, single+"(", basket)
        if (right > 0) and (right>left):
            self.generate2(left, right-1, single+")", basket)
        if left==0 and right ==0:
            basket.append(single)


    # 非递归版本
    def generateParenthesis3(self, n):
        stack = [('(', 1, 0)]

        ans = []

        while len(stack) > 0:
            token, left, right = stack.pop()

            if left + right == 2 * n:
                ans.append(token)
                continue

            if left < n:
                stack.append((token + '(', left + 1, right))

            if left > right:
                stack.append((token + ')', left, right + 1))

        return ans


solution = Solution()
solution.generateParenthesis(3)