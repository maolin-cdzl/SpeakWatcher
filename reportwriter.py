# -*- coding: UTF-8 -*-

import logging
import threading
import datetime
import Queue
from statdata import StatData

class ReportWriter(threading.Thread):
    def __init__(self,path):
        super(ReportWriter,self).__init__()
        self.freport = path + '/report.txt'
        self.fperiod = path + '/report.period.txt'
        self.q = Queue.Queue()

    def run(self):
        while True:
            data = self.q.get(True)
            if isinstance(data,int):        # exit signal
                break;
            if not isinstance(data,StatData):
                continue
            self.write(data)

    def write(self,report):
        with open(self.freport,'a') as f:
            f.write('%s\n' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            f.write('lost: %d\n' % report.lost_count)
            f.write('Request Mic Reply\n')
            for k in sorted(report.rep_map):
                f.write('%d\t%d\n' % (k,report.rep_map[k]))

            f.write('Member Speaking Notify\n')
            for k in sorted(report.notify_map):
                f.write('%d\t%d\n' % (k,report.notify_map[k]))

            f.write('AudioPacket transaction\n')
            for k in sorted(report.ap_map):
                f.write('%d\t%d\n' % (k,report.ap_map[k]))
            f.close()

        avg = 0
        if report.period_ap_count > 0:
            avg = report.period_ap_sum / report.period_ap_count
        with open(self.fperiod,'a') as f:
            f.write('%s\t%d\t%d\t%d\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),report.period_ap_count, avg, report.period_ap_max))
            f.close()

    def report(self,data):
        try:
            self.q.put(data,False)
        except:
            logging.warning('put report to queue failed')
            pass
    
    def stop(self):
        if not self.isAlive():
            return
        self.q.put(0)
        self.join(1.0)
