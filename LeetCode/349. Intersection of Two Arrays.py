#-*-coding:utf-8 -*-
"""
    349. Intersection of Two Arrays
    Directed by user zhongch4g
    current system date 2017/4/16
"""

import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # set保证list里面没有重复元素
        nums1=set(nums1)
        # print nums1
        nums2=set(nums2)
        # print nums2
        # 返回nums1和nums2的交集
        set1 = nums1&nums2
        # print list(list3)
        return list(set1)

instance = Solution()
list1 = [1, 2, 2, 1]
list2 = [2, 2]
print instance.intersection(list1, list2)