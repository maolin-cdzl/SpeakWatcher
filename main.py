#!/usr/bin/python

import os
import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
import daemon
from daemon import runner

from speakwatcher import SpeakerWatcher

DEBUG = False
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def SetupLogger():
    FORMAT = "%(asctime)-15s %(levelname)-8s %(message)s"
    formatter = Formatter(fmt=FORMAT)
    logger = logging.getLogger()

    if DEBUG:
        handle = logging.StreamHandler()
        logger.setLevel(logging.DEBUG)
    else:
        handler = TimedRotatingFileHandler('%s/speak.log' % ROOT_PATH,when="d",interval=1,backupCount=7)
        logger.setLevel(logging.INFO)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

class App:
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '%s/.speakwatcher.pid' % ROOT_PATH
        self.pidfile_timeout = 5
        self.svcs = []

    def run(self):
        watcher = SpeakerWatcher()
        watcher.start(ROOT_PATH,DEBUG)


if __name__ == '__main__':
    SetupLogger()
    app = App()

    if DEBUG:
        app.run()
    else:
        daemon_runner = runner.DaemonRunner(app)
        daemon_runner.do_action()

