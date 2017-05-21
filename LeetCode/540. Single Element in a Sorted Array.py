#-*-coding:utf-8 -*-
"""
    540. Single Element in a Sorted Array
    Directed by user zhongch4g
    current system date 2017/5/21
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Note: Your solution should run in O(log n) time and O(1) space.
        return reduce(lambda x, y:x^y, nums)

    def singleNonDuplicate2(self, nums):
        for i, n in enumerate(nums):
            # print i, n
            if i % 2 == 0:
                if len(nums) == (i+1):
                    return n
                elif n != nums[i+1]:
                    return n
"""
Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""
instance = Solution()
print instance.singleNonDuplicate2([3,3,7,10,10,11,11])