#-*-coding:utf-8 -*-
"""
    551. Student Attendance Record I
    Directed by user zhongch4g
    current system date 2017/4/24
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        'A' : Absent.
        'L' : Late.
        'P' : Present.
        """
        count = {'A':0, 'L':0, 'P':0}
        for i in s:
            count[i] += 1
        s1 = "ALP"
        for char in s1:
            if count[char] == 0:
                count[char] = None
        # print count
        # print count['L']
        # if count['A'] is not None:
        #     if count['A'] <= 1:
        #         return True
        # if count['L'] is not None:
        #     if count['L'] <= 2:
        #         return True
        # return False
        return count['A'] <= 1 and 'LLL' not in s
instance = Solution()
print instance.checkRecord("PPALLL")