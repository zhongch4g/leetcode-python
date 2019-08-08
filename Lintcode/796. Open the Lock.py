#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 12:35 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 796. Open the Lock.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if '0000' == target:
            return 0
        if '0000' in deadends:
            return -1

        visited = {'0000'}
        queue = deque(['0000'])
        step = 0
        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return step
                for i in range(0, 4):
                    tmp = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i + 1:]
                    if tmp not in visited and tmp not in deadends:
                        queue.append(tmp)
                        visited.add(tmp)

                    tmp = curr[:i] + str((int(curr[i]) - 1 + 10) % 10) + curr[i + 1:]
                    if tmp not in visited and tmp not in deadends:
                        queue.append(tmp)
                        visited.add(tmp)
            step += 1


        return -1



deadends = ["2110","2000","0000","2111","1110"]
target = "0012"
solution = Solution()
res = solution.openLock(deadends, target)
print(res)