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
        # new version
        vowels_str = ""
        for chars in s:
            if chars in "aeiouAEIOU":
                vowels_str += chars
        i = 0
        # reverse = ""
        vowels_str_re = vowels_str[::-1]
        print vowels_str_re
        list_s = list(s)
        for j in range(len(list_s)):
            if list_s[j] in "aeiouAEIOU":
                # reverse += vowels_str_re[i]
                # i += 1
                list_s[j] = vowels_str_re[i]
                i += 1
            # else:
            #     reverse += s[j]
        # return reverse
        # print list_s
        return "".join(list_s)

        # sa = [x for x in s]
        # st, end = 0, len(sa) - 1
        # vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        # while st < end:
        #     while st < end and sa[st] not in vowels:
        #         st += 1
        #     while st < end and sa[end] not in vowels:
        #         end -= 1
        #     if st != end:
        #         sa[st], sa[end] = sa[end], sa[st]
        #     st, end = st+1, end-1
        # return "".join(sa)

instance = Solution()
print instance.reverseVowels("hello")