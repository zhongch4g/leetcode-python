#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 11:13 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1380. Log Sorting.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        if not logs:
            return logs

        res = [None] * len(logs)
        letter = []
        index = len(logs) - 1
        for i in range(len(logs) - 1, -1, -1):
            content_i = logs[i].index(' ')
            if content_i + 1 < len(logs[i]) and '0' <= logs[i][content_i + 1]  <= '9':
                res[index] = logs[i]
                index -= 1
            else:
                letter.append(logs[i])
        letter.sort(key=lambda log:(log[log.index(' '):], log[:log.index(' ')]))
        index = 0
        for log in letter:
            res[index] = log
            index += 1
        return res


