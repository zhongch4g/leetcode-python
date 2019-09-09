#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 1:47 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 322. Coin Change.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def coinChange(self, coins, amount: int) -> int:

        return self.search(coins, amount, {})

    def search(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        minimum = sys.maxsize
        for coin in coins:

            number = self.search(coins, amount - coin, memo)
            if 0 <= number < minimum:
                minimum = 1 + number

        memo[amount] = minimum if minimum != sys.maxsize else -1
        return memo[amount]