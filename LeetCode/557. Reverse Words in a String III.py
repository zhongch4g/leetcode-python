"""
    557. Reverse Words in a String III
    Directed by user zhongch4g
    current system date 2017/4/13
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(string):
            return string[::-1]
        srlist = s.split(" ")
        return " ".join(list(map(reverse, srlist)))
instance = Solution()
instance.reverseWords("Let's take LeetCode contest")