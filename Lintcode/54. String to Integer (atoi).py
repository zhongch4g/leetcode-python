#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 4:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 54. String to Integer (atoi).py
# @Software: IntelliJ IDEA

import sys
class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        maxint = 2147483647
        minint = -2147483648
        str = str.strip()
        if str == '':
            return 0
        flag = None
        if str[0] == '+':
            flag = 1
        if str[0] == '-':
            flag = 0

        pure_digit = str[1:] if flag is not None else str[:]
        str = pure_digit
        dot, idx = 0, len(str)
        for n in range(len(str)):
            if str[n] == '.':
                dot += 1
                idx = n
                continue
            if dot > 1 or (dot == 1 and str[n] != '0'):
                return 0
            if str[n] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                idx = n
                break
            # 第一个数字是0 且后面还有数字
            if n == 0 and str[n] == 0 and n + 1 <= len(str):
                return 0

        pure_digit = str[:idx]
        print(pure_digit)

        left = None
        cur = 0

        if flag is None or flag == 1:
            left = maxint
            x = 1
            for i in range(len(pure_digit) - 1, -1, -1):
                d = int(pure_digit[i])
                if x <= 1000000000:

                    left = left - d * x
                    if left < 0:
                        return maxint

                    cur = d * x + cur
                    x = x * 10
        else:
            left = minint
            x = 1
            for i in range(len(pure_digit) - 1, -1, -1):
                d = int(pure_digit[i])
                if x <= 1000000000:
                    left = left + d * x
                    if left >= 0:
                        return minint

                    cur = d * x + cur
                    x = x * 10
            cur = -cur
        return cur

    def atoi2(self, str):
        str = str.strip()
        if str == "" :
            return 0
        i = 0
        sign = 1
        ret = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-' :
            i += 1
            sign = -1

        for i in range(i, length) :
            if str[i] < '0' or str[i] > '9' :
                break
            ret = ret * 10 + int(str[i])
            if ret > sys.maxsize:
                break
        ret *= sign
        if ret >= MaxInt:
            return MaxInt
        if ret < MaxInt * -1 :
            return MaxInt * - 1 - 1
        return ret


solution = Solution()
res = solution.atoi("1234567890123456789012345678901234567890")
print(res)
