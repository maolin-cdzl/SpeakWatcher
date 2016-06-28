# -*- coding: UTF-8 -*-

import sys
import time
import logging
from statdata import StatData

if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time

def current_millis():
    return int(round(default_timer() * 1000))

class SpeakStatistics:
    def __init__(self,loop,speaker,listener,cb):
        self.ap = []
        self.tv_req = 0.0
        self.stat = StatData()
        self.callback = cb

        speaker.on('req-mic',self.onReqMic)
        speaker.on('got-mic',self.onGotMic)
        speaker.on('send-ap',self.onSendAp)
        listener.on('startlisten',self.onStartListen)
        listener.on('recv-ap',self.onRecvAp)

        self.timer = loop.timer(60.0,60.0,self.report)
        self.timer.start()

    def report(self,w,revent):
        rp = self.stat.dump()
        self.stat.resetPeriod()
        self.callback(rp)

    def onReqMic(self,*args,**kwargs):
        self.tv_req = current_millis()

    def onGotMic(self,*args,**kwargs):
        self.stat.rep( current_millis() - self.tv_req )

    def onSendAp(self,*args,**kwargs):
        seq = kwargs['seq']
        if seq is None:
            raise RuntimeError('send-ap event has no seq')
        now = current_millis()
        self.ap.append( (seq,now) )
        
        while len(self.ap) > 10:
            self.ap.pop(0)
            self.stat.lost()

    def onStartListen(self,*args,**kwargs):
        self.stat.notify( current_millis() - self.tv_req )

    def onRecvAp(self,*args,**kwargs):
        seq = kwargs['seq']
        if seq is None:
            raise RuntimeError('recv-ap event has no seq')

        now = current_millis()

        while len(self.ap) > 0:
            s,tv = self.ap.pop(0)
            if s == seq:
                self.stat.ap(now - tv)
                break
            else:
                self.stat.lost()



