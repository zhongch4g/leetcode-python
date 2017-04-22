#-*-coding:utf-8 -*-
"""
    217. Contains Duplicate
    Directed by user zhongch4g
    current system date 2017/4/22
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return True if any value appears at least twice
        # return false if every element is distinct
        counter = dict()
        deci1 = True
        deci2 = False
        for i in nums:
            counter.setdefault(i, 0)
            counter[i] += 1
        if not counter:
            return False
        for count in counter.values():
            if count >= 2:
                return True
        return False

        # one line python solution
        # 根据set容器，会返回list中去重后的list，然后比较长度
        # return len(nums) != len(set(nums))
instance = Solution()
print instance.containsDuplicate([2,14,18,22,22])

