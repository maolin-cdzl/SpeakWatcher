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
    def __init__(self,options):
        self.options = options
        self.loop = None 
        self.speaker = None
        self.listener = None
        self.sploop = None
        self.statis = None
        self.writer = None

    def sig_cb(self,watcher,revents):
        logging.info('signal: %d' % revents)
        watcher.loop.stop(pyev.EVBREAK_ALL)
        self.writer.stop()

    def start(self):
        try:
            self.loop = pyev.default_loop(debug=self.options.get('debug',False))
            sig_int = self.loop.signal(signal.SIGINT,self.sig_cb)
            sig_int.start()
            sig_term = self.loop.signal(signal.SIGTERM,self.sig_cb)
            sig_term.start()

            self.writer = ReportWriter(self.options.get('root_path'))
            self.writer.start()

            accounts = []
            for a in self.options.get('accounts'):
                accounts.append(a)

            builder = ClientBuilder(accounts,self.options,self.addClient)
            builder.start(self.loop)

            self.loop.start()
        finally:
            if self.loop is not None:
                self.loop.stop(pyev.EVBREAK_ALL)
                self.loop = None
            self.builder = None
            self.sploop = None
            self.statis = None
            if self.writer is not None:
                self.writer.stop()
                self.writer = None



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
        



