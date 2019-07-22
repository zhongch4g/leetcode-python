#-*-coding:utf-8 -*-
"""
    169. Majority Element
    Directed by user zhongch4g
    current system date 2017/4/20
"""
import collections


class Solution(object):
    # Tip:the array is non-empty and the majority element always exist in the array
    # http://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html
    #  MJRTY - A Fast Majority Vote Algorithm,
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # most_common([n])
        # 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的
        # numsColl = collections.Counter(nums)
        # return numsColl.most_common()[0][0]
        return collections.Counter(nums).most_common()[0][0]

        # one nice decition to resolve this problem
        # return sorted(num)[len(num)/2]


instance = Solution()
print (instance.majorityElement([1, 2, 3, 3, 2, 2, 2, 2, 2, 2 ,2]))
