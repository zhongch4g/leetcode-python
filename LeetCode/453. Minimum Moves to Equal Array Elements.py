#-*-coding:utf-8 -*-
"""
    453. Minimum Moves to Equal Array Elements
    Directed by user zhongch4g
    current system date 2017/4/15
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 一开始用了for从sums中的最大元素开始循环，但是没有考虑到int32的越界情况，导致Memory Error， 后面没有考虑list里面单元素的情况，
        # 最后就是没有考虑list中的负数，导致list中存在负数的情况错误

        # moves = 0
        # # 当list中只有0个或1个元素的时候
        # if(len(nums) == 1 or len(nums) == 0):
        #     return moves
        # # 将sums从小到大排序
        # sorted_nums = sorted(nums)
        # """
        #     Runtime Error Message:
        #     Line 11: MemoryError
        #     Last executed input:
        #     [-2147483648,-2147483647]
        # """
        # # for i in range(sorted_nums[-1], 100):
        # 从nums最大的元素开始索引
        # i = max(nums)
        # while True:
        # 从nums的最大元素开始索引找最终的结果
        #     list_i = [i for j in range(len(sorted_nums))]
        #
        #     L = list(map(lambda x: x[0]-x[1], zip(list_i, sorted_nums))) # L = [1, 0]
        #     sum = reduce(lambda x,y:x+y, L) # sum = 1
        #
        #     L1 = list(map(lambda x: x[0]+x[1], zip(L, sorted_nums))) # L1 = [-2147483647,-2147483647]
        #
        #     equal_or_not = reduce(lambda x, y: (x == y), map(lambda x:x == L1[0], L1) )
        #     if(sum % (len(sorted_nums) - 1) == 0  and equal_or_not == True and (sum / (len(nums) - 1)) > (max(nums) - min(nums))):
        #         moves = sum / (len(sorted_nums) - 1)
        #         break
        #     i = i + 1
        # return moves

        # 按照过程实现
        cnt = 0
        while True:
            max_nums = max(nums)
            min_nums = min(nums)
            if max_nums == min_nums:
                break
            index = nums.index(max_nums)
            cnt = cnt + 1
            for i in range(len(nums)):
                nums[i] = nums[i] + 1 if i != index else nums[i]
        return cnt
instance = Solution()
print instance.minMoves([-100, 0, 100])
