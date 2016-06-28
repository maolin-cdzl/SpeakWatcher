# -*- coding: UTF-8 -*-

import pyev
import random
from client import Client
from audiogenerator import AudioPacketGenerator

class SpeakLoop:
    def __init__(self,loop,speaker):
        self.loop = loop
        self.speaker = speaker
        self.speaker.on('gotmic',self.onGotMic)
        self.speaker.on('mic-fail',self.onRequestMicFail)
        self.speaker.on('releasemic',self.onReleaseMic)
        self.speaker.on('lostmic',self.onLostMic)

        self.start_timer = self.loop.timer(0.2,0,self.startSpeak)
        self.speaking_timer = self.loop.timer(0.2,0.2,self.sendAudioPacket)
        self.stop_timer = self.loop.timer(1,0,self.stopSpeak);

        self.apgen = AudioPacketGenerator(speaker.userId())

        self.start_timer.start()

    def startSpeak(self,w,revent):
        print('startSpeak')
        if w.active:
            w.stop()
        if self.speaker.isSpeaking():
            w.set(0.2,0)
            w.start()
            return
        self.speaker.requestMic()

    def stopSpeak(self,w,revent):
        print('stopSpeak')
        if w.active:
            w.stop()
        if self.speaking_timer.active:
            self.speaking_timer.stop()

        if self.speaker.isSpeaking():
            self.speaker.releaseMic()

    def sendAudioPacket(self,w,revent):
        print('sendAudioPacket')
        seq,ts,packet = self.apgen.next()
        self.speaker.speak(packet)
        #todo statistics

    def onGotMic(self,client):
        print('onGotMic')
        self.apgen.reset()
        if not self.stop_timer.active:
            self.stop_timer.set(random.uniform(2.0,25.0),0)
        if not self.speaking_timer.active:
            self.speaking_timer.start()

    def onRequestMicFail(self,client):
        print('onRequestMicFail')
        if not self.start_timer.active:
            self.start_timer.start()

    def onReleaseMic(self,client):
        print('onReleaseMic')
        if not self.start_timer.active:
            self.start_timer.start()

    def onLostMic(self,client):
        print('onLostMic')
        if self.speaking_timer.active:
            self.speaking_timer.stop()
        if not self.start_timer.active:
            self.start_timer.start()
        




