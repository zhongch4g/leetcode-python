#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 12:53 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : json_to_html.py
# @Software: IntelliJ IDEA

class Solution:
    def test(self, json):
        self.string = ""
        self.search(json, 0)
        print(self.string)

    def search(self, json, space):


        for k, v in json.items():

            self.string += space * "    " + "<" + str(k) + ">\n"
            if type(json[k]) == dict:
                self.search(json[k], space + 1)
            else:
                self.string += (space + 1) * "    " + str(v) + "\n"
            self.string += space * "    " + "</" + str(k) + ">\n"


solution = Solution()
solution.test({"a": {"b": "1", "c": "2"}})