# -*- coding: UTF-8 -*-

import logging
import struct
import socket
import pyev
from pyee import EventEmitter

import etpacket
import command

STATUS_STUCK                = -1        #login failed etc.
STATUS_OFFLINE              = 1
STATUS_ONLINE               = 2
STATUS_INGROUP              = 3

STATUS_IDLE                 = 0
STATUS_LISTENING            = 1
STATUS_SPEAKING             = 2

class Client(EventEmitter):
    def __init__(self,loop,sock,account,password):
        super(Client,self).__init__()
        logging.debug('Client construct')
        self.procmap = {
            'ptt.rr.LoginAck':          self.onLogin,
            'ptt.rr.JoinGroupAck':      self.onJoinGroup,
            'ptt.rr.LeaveGroupAck':     self.onLeaveGroup,
            'ptt.rr.LogoutAck':         self.onLogout,
            'ptt.push.MemberGetMic':    self.onMemberGetMic,
            'ptt.push.MemberLostMic':   self.onMemberLostMic,
            'ptt.push.LostMic':         self.onLostMic,
            'ptt.rr.RequestMicAck':     self.onRequestMic,
            'ptt.rr.ReleaseMicAck':     self.onReleaseMic,
            'ptt.net.Ping':             self.onPing,
        }
        self.loop = loop
        self.online_status = STATUS_OFFLINE
        self.speak_status = STATUS_IDLE
        self.user = None
        self.group = None
        self.recv_buf = ''
        self.tcp = sock
        self.tcp_io = loop.io(self.tcp,pyev.EV_READ,self.onTcpReadable)
        self.udp = None
        self.udp_io = None
        self.udp_timer = None

        command.Login(self.tcp,account,password)
        self.tcp_io.start()

    def close(self):
        self.online_status = STATUS_OFFLINE
        self.speak_status = STATUS_IDLE
        self.user = None
        self.group = None
        self.recv_buf = ''

        if self.udp_timer:
            self.udp_timer.stop()
            self.udp_timer = None
        if self.udp_io:
            self.udp_io.stop()
            self.udp_io = None
        if self.tcp_io:
            self.tcp_io.stop()
            self.tcp_io = None
        if self.tcp:
            self.tcp.close()
            self.tcp = None
        if self.udp:
            self.udp.close()
            self.udp = None

    def stuck(self):
        self.close()
        self.online_status = STATUS_STUCK
        self.emit('stuck',self)

    def onTcpReadable(self,watcher,revent):
        if revent & pyev.EV_READ:
            data = self.tcp.recv(1024)
            if data is not None and len(data) > 0:
                self.recv_buf += data

                while(True):
                    size,msg = etpacket.unpack(self.recv_buf)
                    if msg is None:
                        break
                    self.recv_buf = self.recv_buf[size:]
                    processer = self.procmap.get(msg.DESCRIPTOR.full_name,None)
                    if processer is not None:
                        processer(msg)

    def onUdpReadable(self,watcher,revent):
        packet = self.udp.recvfrom(1024)
        paytype,seq,ts,ssrc,pay = etpacket.rtp_unpack(packet)

        if paytype == 103:
            self.emit('recv-ap',self,(paytype,seq,ts,ssrc,pay))

    def key(self):
        return self.tcp.fileno()

    def userId(self):
        if self.user is not None:
            return self.user['uid']
        else:
            return 0

    def defaultGroup(self):
        if self.user is not None:
            return self.user['default_group']
        else:
            return 0

    def currentGid(self):
        if self.group is not None:
            return self.group['gid']
        else:
            return 0

    def isSpeaking(self):
        return self.speak_status == STATUS_SPEAKING

    def currentGroupId(self):
        if self.online_status == STATUS_INGROUP:
            return self.group['gid']
        else:
            return 0

    def join(self,gid):
        if self.online_status != STATUS_ONLINE:
            return False
        command.JoinGroup(self.tcp,gid)
        return True

    def leave(self):
        if self.online_status != STATUS_INGROUP:
            return False
        command.LeaveGroup(self.tcp,self.group['gid'])
        return True

    def requestMic(self):
        if self.online_status != STATUS_INGROUP and self.speak_status != STATUS_IDLE:
            return False
        command.RequestMic(self.tcp,self.group['gid'])
        return True

    def releaseMic(self):
        if self.speak_status != STATUS_SPEAKING:
            return False
        command.ReleaseMic(self.tcp,self.group['gid'])
        return True

    def speak(self,packet):
        if self.speak_status != STATUS_SPEAKING:
            return False
        self.udp.sendto(packet,self.group['address'])
        return True

    def onLogin(self,msg):
        if msg.result != 0:
            self.stuck()
            return

        self.online_status = STATUS_ONLINE
        self.user = { 'uid': msg.self.uid, 'name': msg.self.name, 'default_group': msg.conf.default_group }

        self.emit('login',self)

    def onJoinGroup(self,msg):
        if msg.result != 0:
            self.stuck()
            return
        ip = socket.inet_ntoa(struct.pack('!I',msg.group.ip))
        port = msg.group.port
        self.group = { 'gid': msg.group.gid, 'address': (ip,port)}
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.udp_io = self.loop.io(self.udp,pyev.EV_READ,self.onUdpReadable)
        self.udp_io.start()
        self.udp_timer = self.loop.timer(0.01,5.0,self.onUdpTimer)
        self.udp_timer.start()

        self.emit('join',self)
    
    def onLeaveGroup(self,msg):
        self.online_status = STATUS_ONLINE
        self.speak_status = STATUS_IDLE
        self.group = None
        self.udp_timer.stop()
        self.udp_timer = None
        self.udp_io.stop()
        self.udp_io = None
        self.udp.close()
        self.udp = None
        self.emit('leave',self)

    def onLogout(self,msg):
        self.close()
        self.emit('logout',self)

    def onMemberGetMic(self,msg):
        self.speak_status = STATUS_LISTENING
        self.emit('startlisten',self)

    def onMemberLostMic(self,msg):
        self.speak_status = STATUS_IDLE
        self.emit('stoplisten',self)

    def onLostMic(self,msg):
        self.speak_status = STATUS_IDLE
        self.emit('lostmic',self)

    def onRequestMic(self,msg):
        if msg.result == 0:
            self.speak_status = STATUS_SPEAKING
            self.emit('gotmic',self)
        else:
            self.emit('mic-fail',self)

    def onReleaseMic(self,msg):
        self.speak_status = STATUS_IDLE
        self.emit('releasemic',self)

        pass
    def onPing(self,msg):
        command.Pong(self.tcp)

    def onUdpTimer(self,watcher,revent):
        command.UdpHeartBeat(self.udp,self.group['address'],self.user['uid'],self.group['gid'])

