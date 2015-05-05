import main

speak = main.Speaker()

#speak.setVoiceParams("nl", 130)
#speak.speak("hi")

for voice in speak.listVoices():
	print(voice)
	speak.setVoiceParams(voice, 150)
	speak.speak("1")
