#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 12:26 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 526. Load Balancer.py
# @Software: IntelliJ IDEA
import random


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.server = []
        self.hash = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.hash:
            return
        self.server.append(server_id)
        self.hash[server_id] = len(self.server) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.hash:
            return

        index = self.hash[server_id]
        del self.hash[server_id]

        self.hash[self.server[-1]] = index

        self.server[index], self.server[-1] = \
            self.server[-1], self.server[index]

        self.server.pop()




    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return self.server[random.randint(0, len(self.server) - 1)]
