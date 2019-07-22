#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 4:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : wildcard_matching.py
# @Software: IntelliJ IDEA

class Solution():
    def is_match(self, source, parttern):
        """
        :param source:
        :param parttern:
        :return: True or False
        """
        return self.is_correct_match_with_memo(source, 0, parttern, 0, {})

    # 返回source 的索引i之后的字符串是否和parttern 的索引j之后的模式相匹配
    def is_correct_match(self, source, i, parttern, j):
        # 匹配失败的情况
        # 如果source匹配完了而parttern还有
        if len(source) == i:
            for index in range(j, len(parttern)):
                if parttern[index] != "*":
                    return False
            return True

        # 如果parttern匹配完了而source还有
        if len(parttern) == j:
            return False

        # 判断*和？两种情况
        if parttern[j] != "*":
            return self.is_match_single(source[i], parttern[j]) \
                   and self.is_correct_match(source, i + 1, parttern, j + 1)

        # * 匹配串 或者 *匹配空
        return self.is_correct_match(source, i + 1, parttern, j) \
               or self.is_correct_match(source, i, parttern, j + 1)

    def is_correct_match_with_memo(self, source, i, parttern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(source) == i:
            for index in range(j, len(parttern)):
                if parttern[index] != "*":
                    return False
            return True

        if len(parttern) == j:
            return False

        if parttern[j] != "*":
            matched = self.is_match_single(source[i], parttern[j]) \
                   and self.is_correct_match(source, i + 1, parttern, j + 1)

        else:
            matched = self.is_correct_match(source, i + 1, parttern, j) \
               or self.is_correct_match(source, i, parttern, j + 1)

        memo[(i, j)] = matched
        return matched

    def is_match_single(self, s, p):
        return s == p or p == "?"

solution = Solution()
result = solution.is_match("aabbbbbbb", "a*")
print(result)