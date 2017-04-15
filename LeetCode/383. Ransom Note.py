#-*-coding:utf-8 -*-
"""
    383. Ransom Note
    Directed by user zhongch4g
    current system date 2017/4/15
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 将字符串ransomNote, magazine转换成list，然后创建list1的复制
        list1 = list(ransomNote)
        list2 = list(magazine)
        list1_temp = list(ransomNote)
        length = len(list1)
        # 依次取复制的list1的值
        for arg in list1_temp:
            if(arg in list2):
                # 将两个list里面相同的值删除
                list1.remove(arg)
                list2.remove(arg)
        # list1里面如果还含有字符的话则不满足，不含字符则满足
        if(list1 == []):
            return True
        else:
            return False

# Leetcode里面的一个用collection.Counter的一个解答方案，答案很简便
# Counter之间的"-"是 subtract（只保留正数计数的元素）
# def canConstruct(self, ransomNote, magazine):
#     return not collections.Counter(ransomNote) - collections.Counter(magazine)

instance = Solution()
print instance.canConstruct("aa", "aab")