# -*- coding: UTF-8 -*-

import logging
from logging import Formatter
import signal
import pyev
from clientbuilder import ClientBuilder
from speakloop import SpeakLoop
from speakstatistics import SpeakStatistics
from reportwriter import ReportWriter

class SpeakerWatcher:
    def __init__(self):
        self.loop = None 
        self.speaker = None
        self.listener = None
        self.sploop = None
        self.statis = None
        self.writer = None

    def sig_cb(self,watcher,revents):
        watcher.loop.stop(pyev.EVBREAK_ALL)
        self.writer.stop()

    def start(self,path,debug):
        self.loop = pyev.default_loop(debug=debug)
        sig = self.loop.signal(signal.SIGINT,self.sig_cb)
        sig.start()

        self.writer = ReportWriter(path)
        self.writer.start()

        #'16805400212','16805400213','16805400214','16805400215','16805400216','16805400217','16805400218','16805400219','16805400220']
        # accounts = [('16805400210','1'),('16805400211','1')] 
        accounts = [('16805400212','1'),('16805400213','1')] 
        options = {
                'address': ('119.254.211.165',10000),
                #'address': ('192.168.2.13',10008),
                'ingroup': True
        }

        builder = ClientBuilder(accounts,options,self.addClient)

        builder.start(self.loop)

        self.loop.start()

    def addClient(self,client):
        if self.speaker is None:
            logging.debug('speaker ready')
            self.speaker = client
            return
        if self.listener is None:
            if self.speaker.currentGroupId() != client.currentGroupId():
                raise RuntimeError('2 client not in same group')
            logging.debug('listener ready')
            self.listener = client
            self.startTest()
            return
        
        raise RuntimeError('Too many clients')

    def startTest(self):
        self.sploop = SpeakLoop(self.loop,self.speaker)
        self.statis = SpeakStatistics(self.loop,self.speaker,self.listener,self.writer.report)
        



