# -*- coding: UTF-8 -*-

import logging
import random
import pyev
from client import Client
from audiogenerator import AudioPacketGenerator

class SpeakLoop:
    def __init__(self,loop,speaker):
        self.loop = loop
        self.speaker = speaker
        self.speaker.on('got-mic',self.onGotMic)
        self.speaker.on('fail-mic',self.onRequestMicFail)
        self.speaker.on('on-rel-mic',self.onReleaseMic)
        self.speaker.on('lost-mic',self.onLostMic)

        self.start_timer = self.loop.timer(1.0,0,self.startSpeak)
        self.speaking_timer = self.loop.timer(0.2,0.2,self.sendAudioPacket)
        self.stop_timer = self.loop.timer(0.5,0,self.stopSpeak);

        self.apgen = AudioPacketGenerator(speaker.userId())

        self.start_timer.start()

    def startSpeak(self,w,revent):
        logging.debug('startSpeak')
        if self.start_timer.active:
            self.start_timer.stop()
        if self.speaker.isSpeaking():
            return
        self.speaker.requestMic()

    def stopSpeak(self,w,revent):
        logging.debug('stopSpeak')
        if self.stop_timer.active:
            self.stop_timer.stop()
        if self.speaking_timer.active:
            self.speaking_timer.stop()

        if self.speaker.isSpeaking():
            self.speaker.releaseMic()
        if not self.start_timer.active:
            self.start_timer.set(2.0,0)
            self.start_timer.start()

    def sendAudioPacket(self,w,revent):
        seq,ts,packet = self.apgen.next()
        self.speaker.speak(seq,ts,packet)

    def onGotMic(self,client):
        logging.debug('onGotMic')
        self.apgen.reset()
        if not self.stop_timer.active:
            self.stop_timer.set(random.uniform(2.0,25.0),0)
            self.stop_timer.start()
        if not self.speaking_timer.active:
            self.speaking_timer.set(0.2,0.2)
            self.speaking_timer.start()

    def onRequestMicFail(self,client):
        logging.debug('onRequestMicFail')
        if not self.start_timer.active:
            self.start_timer.set(1.0,0)
            self.start_timer.start()

    def onReleaseMic(self,client):
        logging.debug('onReleaseMic')
        if not self.start_timer.active:
            self.start_timer.set(1.0,0)
            self.start_timer.start()

    def onLostMic(self,client):
        logging.debug('onLostMic')
        if self.speaking_timer.active:
            self.speaking_timer.stop()
        if self.stop_timer.active:
            self.stop_timer.stop()
        if not self.start_timer.active:
            self.start_timer.set(1.0,0)
            self.start_timer.start()
        




