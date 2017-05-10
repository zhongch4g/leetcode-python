#-*-coding:utf-8 -*-
"""
    459. Repeated Substring Pattern
    Directed by user zhongch4g
    current system date 2017/5/10
"""
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s) == 1:
        #     return False
        # s_dict = dict()
        # for char in s:
        #     s_dict.setdefault(char, 0)
        #     s_dict[char] += 1
        # print s_dict


        # s_values = set(s_dict.values())
        # count = sum(s_dict.values())
        # print s_dict
        # print s_values
        # if len(s_values) != 1:
        #     return False
        # for i in range(count):
        #     print s[i]
        #     s_dict[s[i]] -= 1
        # # print s_dict
        # after_s_values = set(s_dict.values())
        # if len(after_s_values) != 1:
        #     return False
        # return True
        # print s_dict, len(s_dict)


        # 第一个char是重复字符串的第一个char
        # 最后一个char是重复字符串的最后一个char
        # S1 = S + S
        # 去掉S1中的第一个和最后一个char
        if not str:
            return False

        ss = (str + str)[1:-1]
        print range(10), range(10)[1:-1]
        print str + str, ss
        return ss.find(str) != -1

instance = Solution()
# print instance.repeatedSubstringPattern("asdfasdfasdf")
# print instance.repeatedSubstringPattern("abaababaababaab")
print instance.repeatedSubstringPattern("abcdabcde")
