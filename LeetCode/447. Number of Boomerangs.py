#-*-coding:utf-8 -*-
"""
    447. Number of Boomerangs
    Directed by user zhongch4g
    current system date 2017/4/25
"""
import itertools
import collections
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
        listOfBoomerangs = list(itertools.combinations(points, 3))
        # print listOfBoomerangs
        countBoomerangs = 0
        for pair1 in listOfBoomerangs:
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
    def numberOfBoomrangs1(self, points):
        nums = 0
        for x1, y1 in points:
            distance = collections.defaultdict(int)
            for x2, y2 in points:
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                d = dx * dx + dy * dy
                distance[d] += 1

        nums += sum(n * (n-1) for n in distance.values())
        return nums

# print list(combinations([[0,0], [1,0], [2,0], [3, 0]], 3))
instance = Solution()
print instance.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]) # expect 20

# l = [1, 2, 3]
# print list(combinations_with_replacement(l, 3))
# print list(product(l, repeat = 2))
# print list(itertools.permutations(l, 3))