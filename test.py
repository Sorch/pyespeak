import main
import re
speak = main.Speaker()
import time
import threading

for v in speak.listVoices():
    speak.setVoiceParams(voice = v)
    speak.speak("1")
