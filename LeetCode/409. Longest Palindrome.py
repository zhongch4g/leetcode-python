#-*-coding:utf-8 -*-
"""
    409. Longest Palindrome
    Directed by user zhongch4g
    current system date 2017/4/21
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 问题没有考虑清楚
        # 最后一个temp没有加进去判断
        # s1 = sorted(s)
        # print s1
        # longest = 0
        # temp = 1
        # single = 0
        # if len(s1) == 1:
        #     return 1
        # for i in range(1, len(s1)):
        #     if s1[i] == s1[i - 1]:
        #         temp += 1
        #     else:
        #         if temp % 2 == 0:
        #             longest += temp
        #             temp = 1
        #         elif temp % 2 == 1:
        #             longest += temp - 1
        #             temp = 1
        #             single = 1
        counter, longest = dict(), 0
        single = 0
        for i in s:
            counter.setdefault(i,0)
            counter[i] += 1

        for i in counter.values():
            if i % 2 == 1:
                longest += i-1
                single = 1
            else:
                longest += i

        if single == 1:
            return longest + 1
        else:
            return longest

        # counter, sum = dict(), 0
        # flag = True
        # for i in s:
        #     counter.setdefault(i,0)
        #     counter[i] += 1
        # print counter
        #
        # for v in counter.values():
        #     if v & 1:
        #         sum += v-1
        #         flag = False
        #     else:
        #         sum += v
        #
        # return sum if flag else sum + 1
instance = Solution()
print instance.longestPalindrome("aaaAaaaa") # abccccdd aaaAaaaa
print 4 & 1
print 5 & 1
print 6 & 1
print 7 & 1



