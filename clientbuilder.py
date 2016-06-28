# -*- coding: UTF-8 -*-

import logging
import socket
import pyev
from client import Client

# options: 
#   required: address ('1.2.3.4',100)
#   optional: ingroup True/False default: False
#   optional: parallel int default: 100

class ClientBuilder:
    def __init__(self,accounts,options,callback):
        self.accounts = accounts
        self.options = options
        self.callback = callback
        self.loop = None
        self.watchers = {}
        self.clients = {}

    def start(self,loop):
        self.loop = loop
        parallel = self.options.get('parallel',100)

        for i in range(0, min(parallel,len(self.accounts)) ):
            self.createConnection()
    
    def createConnection(self):
        s = socket.socket()
        s.setblocking(0)
        s.connect_ex(self.options['address'])
        w = self.loop.io(s,pyev.EV_WRITE,self.onConnected,s)
        w.start()
        self.watchers[s.fileno()] = w

    def onConnected(self,w,revent):
        w.stop()
        sock = w.data
        del self.watchers[sock.fileno()]
        e = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if e != 0:
            raise RuntimeError('Can not connect server')
        if pyev.EV_WRITE & revent:
            account,password = self.accounts.pop()
            logging.debug('connection connected')
            client = Client(self.loop,sock,account,password)
            client.on('stuck',self.onClientStuck)
            client.once('login',self.onLogined)
            self.clients[client.key()] = client

    def onClientStuck(self,client):
        raise RuntimeError('Client Stuck,check configure and env')

    def onLogined(self,client):
        logging.debug('client logined')
        if self.options.get('ingroup',False):
            gid = client.defaultGroup()
            if gid is None or gid == 0:
                raise RuntimeError('Client has no default group')
            client.once('join',self.product)
            client.join(gid)
        else:
            self.product(client)

    def product(self,client):
        logging.debug('product client')
        client.remove_listener('stuck',self.onClientStuck)
        del self.clients[ client.key() ]
        self.callback(client)

        parallel = self.options.get('parallel',100)
        for i in range(0, min(parallel,len(self.accounts) - len(self.watchers) - len(self.clients)) ):
            self.createConnection()

