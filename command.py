# -*- coding: UTF-8 -*-

import time
import datetime
#import md5
import hashlib

import sys
import socket
import struct
#import logging

import ptt.ptt_pb2
import ptt.rr_pb2
import etpacket


def Login(sock,account,password):
    msg = ptt.rr_pb2.Login()

    msg.account = account
    m = hashlib.md5()
    m.update(password)
    msg.password = m.hexdigest().upper();
    msg.version = 1
    msg.platform = 'python'
    msg.device = 'pc'
    msg.expect_payload = 103
    msg.accept_payloads._values = (101, 103)

    packet = etpacket.pack(msg)
    sock.send(packet)

def Logout(sock):
    msg = ptt.rr_pb2.Logout()
    packet = etpacket.pack(msg)
    sock.send(packet)

def QueryGroup(sock):
    msg = ptt.rr_pb2.QueryGroup()
    packet = etpacket.pack(msg)
    sock.send(packet)


def JoinGroup(sock,gid):
    msg = ptt.rr_pb2.JoinGroup()
    msg.gid = gid
    packet = etpacket.pack(msg)
    sock.send(packet)

def LeaveGroup(sock,gid):
    msg = ptt.rr_pb2.LeaveGroup()
    msg.gid = gid
    packet = etpacket.pack(msg)
    sock.send(packet)

def RequestMic(sock,gid):
    msg = ptt.rr_pb2.RequestMic()
    msg.gid = gid
    packet = etpacket.pack(msg)
    sock.send(packet)


def ReleaseMic(sock,gid):
    msg = ptt.rr_pb2.ReleaseMic()
    msg.gid = gid
    packet = etpacket.pack(msg)
    sock.send(packet)


def HeartBeat(sock):
    msg = ptt.net_pb2.HeartBeat()
    packet = etpacket.pack()
    sock.send(packet)


def Ping(sock):
    msg = ptt.net_pb2.Ping()
    packet = etpacket.pack(msg)
    sock.send(packet)

def Pong(sock):
    msg = ptt.net_pb2.Pong()
    packet = etpacket.pack(msg)
    sock.send(packet)

def UdpHeartBeat(sock,address,uid,gid):
    msg = ptt.net_pb2.HeartBeat()
    msg.gid = gid
    msg.uid = uid
    packet = etpacket.rtp_pack(100,0,0,uid,etpacket.pack(msg))
    sock.sendto(packet,address)

def UdpPing(sock,address,uid,gid):
    msg = ptt.net_pb2.Ping()
    msg.uid = uid
    msg.gid = gid
    packet = etpacket.rtp_pack(100,0,0,uid,etpacket.pack(msg))
    sock.sendto(packet,address)

def UdpPong(sock,address,uid,gid):
    msg = ptt.net_pb2.Pong()
    msg.uid = uid
    msg.gid = gid
    packet = etpacket.rtp_pack(100,0,0,uid,etpacket.pack(msg))
    sock.sendto(packet,address)

