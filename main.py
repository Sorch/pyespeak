import subprocess
import os
import re

class Speaker(object):
	def __init__(self, voice = "en", speed = 150, pitch = 30, msg = "Enter Some Text"):
		self.voice = voice
		self.speed = int(speed)
		self.msg = msg
		self.voices = []
		self.pitch = int(pitch)

	def setVoiceParams(self, voice = "en", speed = 150, pitch = 30):
		self.voice = voice
		if not isinstance(speed, int):
			self.speed = int(speed)
		else:
			self.speed = speed
		if not isinstance(pitch, int):
			self.pitch = int(pitch)
		else:
			self.pitch = pitch
		if pitch > 300: self.pitch = 30


	def speak(self, msg = "enter some text"):
		self.msg = msg
		FNULL = open(os.devnull, 'w')
		subprocess.call(["espeak", "-v%s" % self.voice, "-s%s" % self.speed, "%s" % self.msg, "-p%s" % self.pitch], stdout=FNULL, stderr=subprocess.STDOUT)


	def listVoices(self):
		""" Lets list the voices """
		data = os.popen("espeak --voices").read().split("\n")[1:-1]
		for vf in data:
			self.voices.append(self.ee(vf)["language"])
		return self.voices

	def ee(self, entry):
		extract_re = re.compile(r"""^\s+(?P<pty>\d+)\s+(?P<language>\S+)\s+(?P<age_gender>\S+)\s+(?P<voice_name>\S+)\s+(?P<file>\S+)(?P<other_languages>.+)""", re.X)
		f = re.match(extract_re, entry).groupdict()
		if f != None:
			return f
