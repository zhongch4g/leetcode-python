#-*-coding:utf-8 -*-
"""
    338. Counting Bits
    Directed by user zhongch4g
    current system date 2017/5/24
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n = 1
        count = 0
        while n <= num:
            n = 2 * n
            count += 1
        count = count
        # print range(-1, 3)
        bitList = [2 ** x for x in range(count)]
        print bitList # [0, 1, 2, 4]
        countList = []
        for c in range(num + 1):
            numOfOne = 0
            for bit in bitList[::-1]:
                if c >= bit:
                    c = c - bit
                    numOfOne += 1
            countList.append(numOfOne)
        return countList

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # find the partern of the problem
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
            # print res

        return res[:num+1]

    # Counting Bits with dp Solution
    # https://leetcode.com/problems/counting-bits/#/solutions

instance = Solution()
print instance.countBits2(17)
# [0, 1, 2, 4, 8, 16, 32]

# [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2]
# [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
"""
0 00000000
1 00000001
2 00000010
3 00000011
4 00000100

5 00000101

6 00000110
7 00000111
8 00001000
9 00001001
10 00001100

"""