import subprocess 
import os
import re

class Speaker(object):
	def __init__(self, voice = "en", speed = 150, msg = None):
		self.voice = voice
		self.speed = int(speed)
		self.msg = msg
		self.voices = []

	def setVoiceParams(self, voice, speed):
		self.voice = voice
		if not isinstance(speed, int):
			self.speed = int(speed)
		else:
			self.speed = speed

	def speak(self, msg):
		self.msg = msg
		FNULL = open(os.devnull, 'w')
		subprocess.call(["espeak", "-v%s" % self.voice, "-s%s" % self.speed, "%s" % self.msg], stdout=FNULL, stderr=subprocess.STDOUT)


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
