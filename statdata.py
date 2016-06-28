# -*- coding: UTF-8 -*-

import copy

class StatData:
    def __init__(self):
        self.lost_count = 0
        self.rep_map = {}
        self.notify_map = {}
        self.ap_map = {}
        self.period_ap_count = 0
        self.period_ap_sum = 0
        self.period_ap_max = 0

    def resetPeriod(self):
        self.period_ap_count = 0
        self.period_ap_sum = 0
        self.period_ap_max = 0

    def rep(self,diff):
        if diff in self.rep_map:
            self.rep_map[diff] += 1
        else:
            self.rep_map[diff] = 1

    def notify(self,diff):
        if diff in self.notify_map:
            self.notify_map[diff] += 1
        else:
            self.notify_map[diff] = 1

    def lost(self):
        self.lost_count += 1

    def ap(self,diff):
        if diff in self.ap_map:
            self.ap_map[diff] += 1
        else:
            self.ap_map[diff] = 1

        self.period_ap_count += 1
        self.period_ap_sum += diff
        self.period_ap_max = max(diff,self.period_ap_max)

    def dump(self):
        return copy.deepcopy(self)

