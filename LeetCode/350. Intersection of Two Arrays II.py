#-*-coding:utf-8 -*-
"""
    350. Intersection of Two Arrays II
    Directed by user zhongch4g
    current system date 2017/4/25
"""
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = dict()
        dict2 = dict()
        for i in nums1:
            dict1.setdefault(i, 0)
            dict1[i] += 1
        for j in nums2:
            dict2.setdefault(j, 0)
            dict2[j] += 1
        compare = 0
        key = []
        relist = []
        if len(nums1) < len(nums2):
            compare = 1
            key = dict1.keys()
        else:
            key = dict2.keys()
        for ke in key:
            count_num = 0
            if ke in dict1.keys() and ke in dict2.keys():
                # if dict1[ke] > dict2[ke]:
                #     count_num = dict2[ke]
                # else:
                #     count_num = dict1[ke]
                # 可以简化语句
                count_num = min(dict1[ke], dict2[ke])
                # relist.append([ke] * count_num)
                for i in range(count_num):
                   relist.append(ke)
        return relist

        # 更简便的解法
        # c1, c2 = Counter(nums1), Counter(nums2)
        # # Counter内的与运算可以直接得到相交元素的字典
        # print c1 & c2
        # return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

instance = Solution()
nums1 = [1, 2, 2, 1, 3]
nums2 = [2, 2, 3]
print instance.intersect(nums1, nums2)

