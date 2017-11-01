#-*-coding:utf-8 -*-
"""
    # @File    : 506. Relative Ranks.py
    # @Author  : zhongch4g
    # @Time    : 2017/11/1 16:14
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        """
        ["Gold Medal", "Silver Medal", "Bronze Medal"]
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        return [i for i in map(lambda x:dict([i for i in zip(sort, rank)])[x], nums)]


    #solution2
    def findRelativeRanks1(self, nums):
        d, ans = {}, [0] * len(nums)
        print(ans)
        for i, x in enumerate(nums):
            # 序号 + 分数
            d[x] = i
        key = sorted(d.keys(), reverse=True)
        for j, x in enumerate(key):
            if j == 0:
                ans[d[x]] = "Gold Medal"
            elif j == 1:
                ans[d[x]] = "Silver Medal"
            elif j == 2:
                ans[d[x]] = "Bronze Medal"
            else:
                ans[d[x]] = str(j + 1)
        return ans


instance = Solution()
print(instance.findRelativeRanks1([5,4,3,2,1]))