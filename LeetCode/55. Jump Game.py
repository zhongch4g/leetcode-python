#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 12:35 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 55. Jump Game.py
# @Software: IntelliJ IDEA


class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return True
        memo = {}
        return self.helper2(nums, 0, memo)

    def helper(self, nums, index, memo):
        if index in memo:
            return memo[index]
        if index == len(nums) - 1:
            return True
        furthest_jump = min(index + nums[index], len(nums) - 1)
        for cur in range(index + 1, furthest_jump + 1):
            if self.helper(nums, cur, memo):
                memo[index] = True
                return True

        memo[index] = False
        return False

    def helper2(self, nums, index, memo):
        if index in memo:
            return memo[index]
        if index >= len(nums) - 1:
            return True

        for cur in range(1, nums[index] + 1):
            if self.helper2(nums, index + cur, memo):
                memo[index] = True
                return True
        memo[index] = False
        return False


    # dp version
    def canJump3(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return True

        length = len(nums)
        memo = [False for i in range(length)]
        memo[-1] = True

        for i in range(length - 1, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < length and memo[i + j]:
                    memo[i] = True
                    break
        print(memo)
        return memo[0] == True


    # Greedy
    def canJump4(self, nums):
        last_pos = len(nums) - 1
        for i in range(last_pos, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


nums = [2,3,1,1,4]
solution = Solution()
res = solution.canJump4(nums)
print(res)