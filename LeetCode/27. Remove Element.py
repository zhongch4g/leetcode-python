#-*-coding:utf-8 -*-
"""
    27. Remove Element
    Directed by user zhongch4g
    current system date 2017/5/4
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # delete value = val from nums

        # define index j
        j = len(nums) - 1
        # for i in range(len(nums)):
        count = 0
        for num in nums:
            if num == val:
                count += 1
        i = 0
        while i < j:
            # find num[j] != val
            while nums[j] == val and i < j:
                j -= 1
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            else:
                i += 1
        return len(nums) - count

instance = Solution()
# nums = [3,2,4,2,5,5,2,3]
nums = [3, 3]
print instance.removeElement(nums, 3)