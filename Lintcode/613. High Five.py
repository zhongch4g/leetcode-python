#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 7:59 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 613. High Five.py
# @Software: IntelliJ IDEA

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):

        result = {}
        hash = {}
        for rec in results:
            if rec.id not in hash:
                hash[rec.id] = []
            heapq.heappush(hash[rec.id], rec.score)

            if len(hash[rec.id]) > 5:
                heapq.heappop(hash[rec.id])

        print(hash)
        for k, v in hash.items():
            result[k] = sum(v)

        return result


solution = Solution()
solution.highFive([Record(1,100),Record(1,100),Record(1,100),Record(1,100),Record(1,20),Record(1,100)])
