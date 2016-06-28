# -*- coding: UTF-8 -*-
import random
import etpacket

class AudioPacketGenerator:
    def __init__(self,uid):
        if uid is None or uid == 0:
            raise RuntimeError('Invalid speaker uid')
        self.uid = uid
        self.seq = random.randint(0,65536)
        self.ts = random.randint(0,65536)
        self.data = bytes(bytearray(102))

    def reset(self):
        self.seq = random.randint(0,65536)
        self.ts = random.randint(0,65536)

    def next(self):
        self.seq = (self.seq + 1) % 65536
        self.ts += 1600
        packet = etpacket.rtp_pack(103,self.seq,self.ts,self.uid,self.data)
        return (self.seq,self.ts,packet)
