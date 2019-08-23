#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 9:47 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 937. Reorder Log Files.py
# @Software: IntelliJ IDEA


class Solution:
    def reorderLogFiles(self, logs):

        length = len(logs)
        if length <= 1:
            return logs
        result = [None] * length
        ridx = length - 1
        letter_logs = []
        for i in range(length - 1, -1, -1):
            space_i = logs[i].index(" ")
            if space_i + 1 < length and "0" <= logs[i][space_i + 1] <= "9":
                result[ridx] = logs[i]
                ridx -= 1
            else:
                letter_logs.append(logs[i])
        letter_logs.sort(key = lambda log: (log[log.index(' '):], log[:log.index(" ")]))
        result[:len(letter_logs)] = letter_logs
        return result
