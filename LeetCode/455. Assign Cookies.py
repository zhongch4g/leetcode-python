"""
    455. Assign Cookies
    Directed by user zhongch4g
    current system date 2017/4/13
"""

# each cookie j has a size sj
# If sj >= gi, we can assign the cookie j to the child i
# maximize the number of your content children and output the maximum number.

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cnt = 0
        g1 = sorted(g)
        s1 = sorted(s)
        i, j = 0, 0
        leng = len(g1)
        lens = len(s1)
        while(i < leng and j < lens):
            if(g1[i] <= s1[j]):
                cnt = cnt + 1
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return cnt

list1 = [1, 2]
list2 = [1, 2, 3]
instance = Solution()
print instance.findContentChildren(list1, list2)