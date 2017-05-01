#-*-coding:utf-8 -*-
"""
    35. Search Insert Position
    Directed by user zhongch4g
    current system date 2017/5/1
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pre = 0
        last = len(nums) - 1
        def binarySearch(nums, pre, last, target):
            mid = (pre + last)/2
            if pre > last:
                return pre
            if target < nums[mid]:
                return binarySearch(nums, pre, mid - 1, target)
            if target > nums[mid]:
                return binarySearch(nums, mid + 1, last, target)
            return mid
        return binarySearch(nums, pre, last, target)

instance = Solution()
nums = [1,3,5,6]
print instance.searchInsert(nums, 2)