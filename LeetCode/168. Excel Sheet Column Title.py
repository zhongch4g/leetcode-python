#-*-coding:utf-8 -*-
"""
    168. Excel Sheet Column Title
    Directed by user zhongch4g
    current system date 2017/4/18
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {'0':'Z', '1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J', '11':'K', '12':'L', '13':'M',
                '14':'N', '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S', '20':'T','21':'U', '22':'V', '23':'W', '24':'X', '25':'Y'}
        string = ""
        if n <= 26:
            string = dict[str(n % 26)]
            return string[::-1]
        while True:
            if n > 0:
                string = string + dict[str(n % 26)]
                if n % 26 is 0:
                    n = (n - 26)/26
                else:
                    n = (n - (n % 26))/26
            else:
                return string[::-1]
    def convertToTitle1(self, num):
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))

instance = Solution()
print instance.convertToTitle(52)
