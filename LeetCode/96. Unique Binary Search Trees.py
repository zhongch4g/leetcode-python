#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 10:10 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 96. Unique Binary Search Trees.py
# @Software: IntelliJ IDEA


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]


    def numTrees2(self, n: int) -> int:
        return self.countTrees(n, {})

    # recursion & search
    def countTrees(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n == 1:
            return 1

        Result = 0
        for i in range(n):
            LeftTrees = self.countTrees(i, memo)
            RightTrees = self.countTrees(n - i - 1, memo)
            Result += LeftTrees * RightTrees
        memo[n] = Result
        return Result


    def numTrees3(self, n: int) -> int:
        nums = {}
        nums[0] = 1
        nums[1] = 1
        def search(n):
            if n in nums:
                return nums[n]
            sum = 0
            for i in range(1, n+1):
                sum += search(i-1) * search(n-i)
            nums[n] = sum
            return sum
        return search(n)

solution = Solution()
res = solution.numTrees(3)
print(res)