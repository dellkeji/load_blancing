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
(1, 4, 2)  b                (1, -3, 1)
(5, -1, 3) a                (-2, -1, 3)
(2, 1, 4)  c                (2, 1, -3)
(6, 3, -2) a                (-1, 3, -2)
(3, 5, -1) b                (3, -2, -1)
(7, 0, 0)  a                (0, 0, 0)
"""
__author__ = "bellkeyang"


SERVER_WEIGHT = {'a': 4, 'b': 2, 'c': 1}


class RoundRobin(object):

    def __init__(self, server):
        self.total = sum(SERVER_WEIGHT.values())

    def get_best_server(self, pre_server_weight=SERVER_WEIGHT):
        # 根据当前权重获取最佳
        sorted_server_weight = sorted(
            pre_server_weight.iteritems, key=lambda x: x[1], reverse=True
        )

        # 得当当前的权重
        for key, val in SERVER_WEIGHT.iteritems():
            SERVER_WEIGHT[key] = val - self.total

        # 返回
        return sorted_server_weight[0][0]

