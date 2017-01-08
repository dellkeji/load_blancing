#-*- coding:utf-8 -*-
"""
round robin with smooth weight for load blancing

algorithm description:
on each peer selection we increase current_weight of each eligible peer by its weight,
select peer with greatest current_weight and reduce its current_weight by total number of weight points distributed
among peers.
"""
__author__ = "bellkeyang"


class RoundRobin(object):

    def __init__(self, server):
        self.server = server

    def get_best_weight(self, best_server):
        total = 0
        for name, value in self.server.iteritems():
            value['curr_weight'] += value['weight']
            total += value['curr_weight']
            if value['curr_weight'] > best_server['curr_weight']:
                best_server = {'name': name, 'curr_weight': value['curr_weight']}

        value['curr_weight'] -= total
        return best_server

