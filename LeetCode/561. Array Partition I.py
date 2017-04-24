#-*-coding:utf-8 -*-
"""
    561. Array Partition I
    Directed by user zhongch4g
    current system date 2017/4/24
"""
from itertools import combinations
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """生成排列可以用product：

        from itertools import product
        l = [1, 2, 3]
        print list(product(l, l))
        print list(product(l, repeat=4))
        组合的话可以用combinations：
        from itertools import combinations
        print list(combinations([1,2,3,4,5], 3))
        """
        # misleading
        # if len(nums) == 2:
        #     return min(nums)
        # list1 = sorted(list(combinations(nums, 2)))
        # print list1, len(list1)
        # print list1[(len(list1) - 1)/2]
        # i = (len(list1) - 1)/2
        # j = (len(list1) - 1)/2 + 1
        # max_pair = 0
        # while(i >= 0 and j <= len(list1) - 1):
        #     if max_pair < min(sum(list1[i]), sum(list1[j])):
        #         max_pair = min(sum(list1[i]), sum(list1[j]))
        #     i -= 1
        #     j += 1
        # return max_pair
        #print sorted(nums)[::2]
        return sum(sorted(nums)[::2])
instance = Solution()
# 只有两组数
# print instance.arrayPairSum([1, 3, 4, 5]) # 2 * n (n == 2) # [1, 2, 3, 4, 5, 6]
print instance.arrayPairSum([1, 2, 3, 4, 5, 6])