#-*-coding:utf-8 -*-
"""
    26. Remove Duplicates from Sorted Array
    Directed by user zhongch4g
    current system date 2017/5/9
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums))
        # print nums
        # return len(nums)
        # print range(1, len(nums))
        i = 0
        length = len(set(nums))
        if length == len(nums):
            return length
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                temp = nums[i]
                del nums[i]
                i -= 1
                nums.append(temp)
            i += 1
        print nums
        return len(list(set(nums)))

        # More quickly Solution
        # Two Pointers?
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1
        """

instance = Solution()
# print instance.removeDuplicates([1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6])
print instance.removeDuplicates([1, 1])