#! /usr/bin/env python

import speech_recognition as spr
import pyvona
import snowboydecoder
import subprocess
from creds import *
import tempfile


def rec():
	detector.terminate()
	r = spr.Recognizer()
	with spr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
	return audio


def tts(text):
	v = pyvona.create_voice(ivonaAccessKey, ivonaSecretKey)
	v.codec = 'mp3'
	v.voice_name = 'Amy'
	v.region = 'eu-west'
	v.fetch_voice(text, './response.mp3')
	

def sr(audio, agent):
	r = spr.Recognizer()
	resp = r.recognize_google(audio)
	return "You asked {}, {}".format(agent, str(resp))


def play(audio_file):
	return_code = subprocess.call(["afplay", audio_file])

	
def echo(agent):
	print "{} Invoked".format(agent)
	audio = rec()
	print "."
	text = sr(audio, agent)
	print "."
	print text
	resp = tts(text)
	print "."
	play('./response.mp3')
	print "."
	global detector
	detector = snowboydecoder.HotwordDetector(models, sensitivity=0.4, audio_gain=1)
	detector.start(callbacks)
	
def moneypenny():
	echo('moneypenny')

def alexa():
	echo('alexa')
	
def snowboy():
	echo('snowboy')

def jarvis():
	echo('jarvis')
	
models = ["alexa.pmdl", "moneypenny.pmdl", "snowboy.umdl", "jarvis.pmdl"]
callbacks = [alexa, moneypenny, snowboy, jarvis]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.4, audio_gain=1)
detector.start(detected_callback=callbacks)



