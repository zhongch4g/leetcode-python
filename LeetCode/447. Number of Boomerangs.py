#-*-coding:utf-8 -*-
"""
    447. Number of Boomerangs
    Directed by user zhongch4g
    current system date 2017/4/25
"""
import itertools
import collections
from itertools import combinations
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(vector1,vector2):
            d=0;
            for a,b in zip(vector1,vector2):
                d+=(a-b)**2;
            return d

        # 得到长度为3的不重复子序列
        listOfBoomerangs = list(itertools.combinations(points, 3))
        countBoomerangs = 0
        for pair1 in listOfBoomerangs:
            # pair1 是否能构成等腰三角形
            if len(set([distance(pair1[0], pair1[1]), distance(pair1[0], pair1[2]), distance(pair1[1], pair1[2])])) != 3:
                continue

            newlist = list(itertools.permutations(pair1, 3))
            # print newlist, " ---- "
            for pair in newlist:
                # print pair[0][0] - pair[1][0], pair[0][0] - pair[2][0], pair[0][1] - pair[1][1], pair[0][1] - pair[2][1]
                # print abs(pair[0][0] - pair[1][0]), abs(pair[0][0] - pair[2][0])
                # if abs(pair[0][0] - pair[1][0]) == abs(pair[0][0] - pair[2][0]) and abs(pair[0][1] - pair[1][1]) == abs(pair[0][1] - pair[2][1]):

                if distance(pair[0], pair[1]) == distance(pair[0], pair[2]):
                    countBoomerangs += 1
        return countBoomerangs

    # clear version
    # "For every point, there are k points with distance d, so there are k*(k-1) pairwise with distance d."!!!
    def numberOfBoomrangs1(self, points):
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f * f + s * s] = 1 + cmap.get(f * f + s * s, 0)
            print(cmap)
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res

# print(list(combinations([[0,0], [1,0], [2,0], [3, 0]], 3)))
instance = Solution()
print (instance.numberOfBoomrangs1([[0,0],[2,0],[-2,0],[0,2],[0,-2]])) # expect 20

# l = [1, 2, 3]
# print list(combinations_with_replacement(l, 3))
# print list(product(l, repeat = 2))
# print list(itertools.permutations(l, 3))