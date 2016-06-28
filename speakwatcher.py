import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
import signal
import pyev
from clientbuilder import ClientBuilder

def sig_cb(watcher,revents):
    watcher.loop.stop(pyev.EVBREAK_ALL)

class SpeakerWatcher:
    def __init__(self):
        self.loop = None 
        self.watchers = []
        self.speaker = None
        self.listener = None

    def start():
        self.loop = pyev.default_loop(debug=True)
        sig = self.loop.signal(signal.SIGINT, sig_cb)
        sig.start()
        self.watchers.append(sig)

        accounts = [('16805400210','1'),('16805400211','1')] #'16805400212','16805400213','16805400214','16805400215','16805400216','16805400217','16805400218','16805400219','16805400220']
        options = {
                'address': ('119.254.211.165',10000),
                'ingroup': True
        }

        builder = ClientBuilder(accounts,options,self.addClient)

        builder.start(self.loop)

        self.loop.start()

    def addClient(self,client):
        if self.speaker is None:
            logging.debug('speaker ready')
            self.speaker = client
        elif self.listener is None:
            if self.speaker.currentGroup() != client.currentGroup():
                raise RuntimeError('2 client not in same group')
            logging.debug('listener ready')
            self.listener = client
        else:
            raise RuntimeError('Too many clients')
        
        timer = self.io.timer(,0,self.onSpeakTimer)
        timer.start()
        self.watchers.append(timer)



def SetupLogger(path):
    FORMAT = "%(asctime)-15s %(levelname)-8s %(message)s"
    formatter = Formatter(fmt=FORMAT)

    logger = logging.getLogger()
    handler = TimedRotatingFileHandler(path,when="d",interval=1,backupCount=7)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    SetupLogger('./speak.log')
    watcher = SpeakerWatcher()
    watcher.start()
