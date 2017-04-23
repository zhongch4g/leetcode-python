#-*-coding:utf-8 -*-
"""
    401. Binary Watch
    Directed by user zhongch4g
    current system date 2017/4/23
"""
from itertools import combinations


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        """
        生成排列可以用product：

        from itertools import product
        l = [1, 2, 3]
        print list(product(l, l))
        print list(product(l, repeat=4))
        组合的话可以用combinations：

        from itertools import combinations
        print list(combinations([1,2,3,4,5], 3))
        """
        # hours最多可以亮三个LED灯 minutes最多可以亮五个LED灯
        hours = {0:[0], 1:[[1], [2], [4], [8]], 2:[[1, 2], [1, 4], [1, 8], [2, 4], [2, 8]], 3:[[1, 2, 4], [1, 2, 8]]}
        minutes = {0:[0],
                   1:[[1], [2], [4], [8], [16], [32]],
                   2:[[1, 2], [1, 4], [1, 8], [1, 16], [1, 32], [2, 4], [2, 8], [2, 16], [2, 32], [4, 8], [4, 16], [4, 32], [8, 16], [8, 32], [16, 32]],
                   3:[[1, 2, 4], [1, 2, 8], [1, 2, 16], [1, 2, 32], [1, 4, 8], [1, 4, 16], [1, 4, 32], [1, 8, 16], [1, 8, 32], [1, 16, 32], [2, 4, 8], [2, 4, 16], [2, 4, 32],
                      [2, 8, 16], [2, 8, 32], [2, 16, 32], [4, 8, 16], [4, 8, 32], [4, 16, 32], [8, 16, 32]],
                   4:[[1, 2, 4, 8], [1, 2, 4, 16], [1, 2, 4, 32], [1, 2, 8, 16], [1, 2, 8, 32], [1, 2, 16, 32], [1, 4, 8, 16], [1, 4, 8, 32], [1, 4, 16, 32], [1, 8, 16, 32], [2, 4, 8, 16], [2, 4, 8, 32],
                      [2, 4, 16, 32], [2, 8, 16, 32]],
                   5:[[1, 2, 4, 8, 16], [1, 2, 4, 8, 32], [1, 2, 4, 16, 32], [1, 2, 8, 16, 32]]}

        # hours = dict()
        # minutes = dict()
        # hour1 = [1, 2, 4, 8]
        # minute1 = [1, 2, 4, 8, 16, 32]
        # list11 = []
        # list22 = []
        # for i in range(3):
        #     hours.setdefault(i, [])
        #     temp_list1 = list(combinations(hour1, i))
        #     for index in temp_list1:
        #         if sum(index) < 12:
        #            list11.append(index)
        #     hours[i] = list11
        # for j in range(5):
        #     minutes.setdefault(j, [])
        #     temp_list2 = list(combinations(minutes, i))
        #     for index in temp_list2:
        #         if sum(index) < 59:
        #             list22.append(index)
        #     minutes[j] = list22

        # print hours
        # print "-------------"
        # print minutes

        list1 = []
        for hour in hours.keys():
            for minute in minutes.keys():
                if hour + minute == num:
                    for led1 in hours[hour]:
                        for led2 in minutes[minute]:
                            s1 = ""
                            if led1 == 0:
                                s1 = "0:"
                            else:
                                s1 = str(sum(led1)) + ':'
                            s2 = ""
                            if led2 == 0:
                                s2 = "00"
                            elif sum(led2) < 10 and led2 is not 0:
                                s2 = "0" + str(sum(led2))
                            else:
                                s2 = str(sum(led2))
                            s = s1 + s2
                            list1.append(s)
        return list1

        # simple python resolve
        # 因为二进制手表显示的是二进制位，所以哪个二进制亮可以置为1
        # return ['%d:%02d' % (h, m)
        #     for h in range(12) for m in range(60)
        #     if (bin(h) + bin(m)).count('1') == num]
instance = Solution()
# print instance.readBinaryWatch(2)
for i in range(6):
    print list(combinations([1, 2, 4, 8, 16, 32], i))