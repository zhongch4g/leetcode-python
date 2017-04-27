#-*-coding:utf-8 -*-
"""
    415. Add Strings
    Directed by user zhongch4g
    current system date 2017/4/27
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """
        1、The length of both num1 and num2 is < 5100.
        2、Both num1 and num2 contains only digits 0-9.
        3、Both num1 and num2 does not contain any leading zero.
        4、You must not use any built-in BigInteger library or convert the inputs to integer directly.
        """
        # 首先确定两个字符串中比较小的串的长度
        min_len = min(len(num1), len(num2))
        string = ""
        # 初始化进位carry为0
        carry = 0
        for i in range(-min_len, 0)[::-1]:
            # 将进行计算的数字从str类型转换成int型
            n1, n2 = int(num1[i]), int(num2[i])
            # print n1, n2
            # 判定是否需要进位
            sumOfn = n1 + n2 + carry
            if sumOfn >= 10:
                on = (sumOfn) % 10
                carry = (sumOfn) / 10
            else:
                on = sumOfn
                carry = 0
            string = str(on) + string
        # print string

        abs_len = abs(len(num1) - len(num2))
        tempstr = ""
        if len(num1) > len(num2):
            tempstr = num1[:abs_len]
        # print carry
        elif len(num1) == len(num2):
            if not carry:
                return string
            else:
                return str(carry) + string
        else:
            tempstr = num2[:abs_len]
        for j in range(-abs_len, 0)[::-1]:
            # print tempstr[j]
            if carry == 0:
                return tempstr + string
            else:
                sumOf = int(tempstr[j]) + carry
                if sumOf >= 10:
                    on = (sumOf) % 10
                    carry = (sumOf) / 10
                else:
                    on = sumOf
                    carry = 0
                string = str(on) + string
                if carry == 0:
                    return tempstr[:j] + string
        return str(carry) + string
        # if len(num1) > len(num2):
        #     print num1[:abs_len - 1], str(carry + int(num1[abs_len - 1])), string
        #     string = num1[:abs_len - 1] + str(carry + int(num1[abs_len - 1])) + string
        # else:
        #     string = num2[:abs_len - 1] + str(carry + int(num2[abs_len - 1])) + string
        # return string


instance = Solution()
s1 = "5099"
s2 = "99"
print instance.addStrings(s1, s2)
# s1 = "1234"
# s2 = "9"
# print range(-9, 0)[::-1]