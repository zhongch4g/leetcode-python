#-*-coding:utf-8 -*-
"""
    345. Reverse Vowels of a String
    Directed by user zhongch4g
    current system date 2017/5/6
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 最后一个用例超时
        # vowels_str = ""
        # for chars in s:
        #     if chars in "aeiouAEIOU":
        #         vowels_str += chars
        # print vowels_str
        # i = 0
        # reverse = ""
        # vowels_str_re = vowels_str[::-1]
        # for j in range(len(s)):
        #     if s[j] in "aeiouAEIOU":
        #         reverse += vowels_str_re[i]
        #         i += 1
        #     if s[j] not in "aeiouAEIOU":
        #         reverse += s[j]
        # return reverse
        sa = [x for x in s]
        st, end = 0, len(sa) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while st < end:
            while st < end and sa[st] not in vowels:
                st += 1
            while st < end and sa[end] not in vowels:
                end -= 1
            if st != end:
                sa[st], sa[end] = sa[end], sa[st]
            st, end = st+1, end-1
        return "".join(sa)

instance = Solution()
print instance.reverseVowels("hello")