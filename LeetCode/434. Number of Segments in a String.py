#-*-coding:utf-8 -*-
"""
    434. Number of Segments in a String
    Directed by user zhongch4g
    current system date 2017/5/9
"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.split(" ")
        return list1

        """
        字符串里有三个去空格的函数
        strip 同时去掉左右两边的空格
        lstrip 去掉左边的空格
        rstrip 去掉右边的空格

        %% 1.采用不带参数的split()，它会把所有空格（空格符、制表符、换行符）当作分隔符。
           2.filter(None, s.split(' '))

        关于filter()方法的使用说明：

        filter(...)
        filter(function or None, sequence) -> list, tuple, or string

        Return those items of sequence for which function(item) is true. If
        function is None, return the items that are true. If sequence is a tuple
        or string, return the same type, else return a list.
        """
        # return len(s.split())
        # return len(filter(None, s.split()))

        if not s: return 0
        # # print [ i for i in s.split(' ') if i!='']
        return len([ i for i in s.split(' ') if i!=''])

instance = Solution()
print instance.countSegments(" ,  ,  ,  ,        my name is")