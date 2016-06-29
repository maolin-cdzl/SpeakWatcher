#!/usr/bin/python

import os
import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
import daemon
from daemon import runner

from speakwatcher import SpeakerWatcher

def SetupLogger(options):
    FORMAT = "%(asctime)-15s %(levelname)-8s %(filename)-16s %(message)s"
    formatter = Formatter(fmt=FORMAT)
    logger = logging.getLogger()

    if options.get('debug',False):
        handler = logging.StreamHandler()
        logger.setLevel(logging.DEBUG)
    else:
        handler = TimedRotatingFileHandler('%s/speak.log' % options.get('root_path'),when="d",interval=1,backupCount=7)
        logger.setLevel(logging.INFO)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

class App:
    def __init__(self,options):
        self.options = options
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '/tmp/speakwatcher.pid'
        self.pidfile_timeout = 5
        self.svcs = []

    def run(self):
        watcher = SpeakerWatcher(self.options)
        watcher.start()

# options: 
#   requried: root_path app root path
#   required: address ('1.2.3.4',100)
#   required: account tuple list
#   optional: builder_join_group True/False default: False
#   optional: builder_parallel int default: 100
#   optional: hack_group_ip ip string or None
#   optional: debug default False

# avalid account:
#   '16805400210','16805400211','16805400212','16805400213','16805400214','16805400215','16805400216','16805400217','16805400218','16805400219','16805400220']


options = {
    'root_path': os.path.dirname(os.path.abspath(__file__)),
    'debug': True,
    #'address': ('192.168.2.13',10008),
    #'address': ('119.254.211.165',10000),
    'address': ('219.148.21.125',10002),
    'accounts': [('18900010004','1'),('18900010005','1')], 
    'builder_join_group': True,
    #'hack_group_ip': '127.0.0.1'
}

if __name__ == '__main__':
    SetupLogger(options)
    app = App(options)

    if options.get('debug',False):
        app.run()
    else:
        daemon_runner = runner.DaemonRunner(app)
        daemon_runner.do_action()

