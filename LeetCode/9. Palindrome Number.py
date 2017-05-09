#-*-coding:utf-8 -*-
"""
    9. Palindrome Number
    Directed by user zhongch4g
    current system date 2017/5/9
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if x < 0:
            return False
        remainder = x % 10
        x = x / 10
        if x == 0:
            return True
        if remainder == 0:
            return False
        countBit = 1
        while x > 0:
            remainder = remainder ^ (x % 10)
            x = x / 10
            countBit += 1
        # print countBit
        if countBit % 2 == 0 and remainder == 0 and (temp % 10) == (temp / 10**(countBit - 1)):
            return True
        elif countBit % 2 == 1:
            countBit = countBit / 2
            if (temp / (10 ** countBit)) % 10 == remainder:
                return True
        return False


        # countBit = countBit / 2
        # # print countBit
        # print (temp / (10 ** countBit)) % 10
        # if remainder == 0 or (temp / (10 ** countBit)) % 10 == remainder:
        #     return True
        # else:
        #     return False

# 3 0011
# 2 0010
# 1 0001
instance = Solution()
print instance.isPalindrome(11)

# 10
