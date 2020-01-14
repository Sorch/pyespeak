import main
speak = main.Speaker()

for v in speak.listVoices():
    speak.setVoiceParams(voice = v)
    speak.speak("1")
print("speaking")
