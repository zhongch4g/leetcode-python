#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 12:18 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1175. Prime Arrangements.py
# @Software: IntelliJ IDEA


import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        MOD = 10**9 + 7
        count = 0
        for i in range(2, n + 1):
            if self.check(i):
                count += 1
        ans = 1
        no = n - count
        while count != 1:
            ans = ((ans % MOD) * (count % MOD)) % MOD
            count -= 1

        while no != 1:
            ans = ((ans % MOD) * (no % MOD)) % MOD
            no -= 1
        return ans

    def check(self, n):
        if n < 3:
            return n > 1
        if n % 2 == 0:
            return False
        sqrt = int(math.sqrt(n))
        for i in range(2, n //2):
            if n % i == 0:
                return False
        return True