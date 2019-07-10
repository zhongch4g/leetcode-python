#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 6:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 12. Integer to Roman.py
# @Software: IntelliJ IDEA


class Solution:
    def intToRoman(self, num):
        count_bit = 0
        roman = ''
        while num != 0:
            cur = num % 10
            num = num // 10

            count_bit += 1
            if count_bit == 1:
                if cur <= 3:
                    roman = cur * 'I' + roman
                elif 4 <= cur <= 8:
                    if cur > 5:
                        roman = 'V' + (cur-5) * 'I' + roman
                    elif cur < 5:
                        roman = 'IV' + roman
                    else:
                        roman = 'V' + roman
                else:
                    roman = 'IX' + roman

            elif count_bit == 2:
                if cur <= 3:
                    roman = cur * 'X' + roman
                elif 4 <= cur <= 8:
                    if cur > 5:
                        roman = 'L' + (cur-5) * 'X' + roman
                    elif cur < 5:
                        roman = 'XL' + roman
                    else:
                        roman = 'L' + roman
                else:
                    roman = 'XC' + roman
            elif count_bit == 3:
                if cur <= 3:
                    roman = cur * 'C' + roman
                elif 4 <= cur <= 8:
                    if cur > 5:
                        roman = 'D' + (cur-5) * 'C' + roman
                    elif cur < 5:
                        roman = 'CD' + roman
                    else:
                        roman = 'D' + roman
                else:
                    roman = 'CM' + roman
            elif count_bit == 4:
                if cur <= 3:
                    roman = cur * 'M' + roman

        return roman

    # 空间节省时间，速度最快
    def intToRoman2(self, num: int) -> str:
        rom = { 1000:'M', 900:'CM', 500:'D',400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL',
                10:'X', 9:'IX', 5:'V', 4: 'IV',1:'I'}

        output = ''

        for r in rom.keys():
            while r <= num:
                num -= r
                output += rom[r]
        return output


"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
solution = Solution()
res = solution.intToRoman(1994)
print(res)