#-*- coding:utf-8 -*-
"""
round robin with smooth weight for load blancing

algorithm description:
on each peer selection we increase current_weight of each eligible peer by its weight,
select peer with greatest current_weight and reduce its current_weight by total number of weight points distributed
among peers.

init data (4, 2, 1)

before     select item      after
(4, 2, 1)  a                (-3, 2, 1)
(1, 4, 1)  b                (1, -3, 1)
(5, -1, 3) a                (-2, -1, 3)
(2, 1, 4)  c                (2, 1, -3)
(6, 3, -2) a                (-1, 3, -2)
(3, 5, -1) b                (3, -2, -1)
(7, 0, 0)  a                (0, 0, 0)
"""
__author__ = "bellkeyang"


class RoundRobin(object):

    def __init__(self, server):
        self.server = server

    def get_best_weight(self, best_server):
        total = 0
        best_name = ''
        for name, value in self.server.iteritems():
            value['curr_weight'] += value['weight']
            total += value['curr_weight']
            if value['curr_weight'] > best_server['curr_weight']:
                best_server = {name: {'curr_weight': value['curr_weight']}}
                best_name = name

        self.server[best_name]['curr_weight'] -= total
        return best_server

