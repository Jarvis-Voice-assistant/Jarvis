import os
import sys
import time
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz

speak_engine = pyttsx3.init()
speak_engine.say("Hello, sir! Do you want something?")
speak_engine.runAndWait()
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	query = r.recognize_google(audio)
	comparision = {
	"compare_time" : fuzz.token_set_ratio(query.lower(), "time"),
	"compare_date" : fuzz.token_set_ratio(query.lower(), "date"),
	"compare_goodbye" : fuzz.token_set_ratio(query.lower(), "goodbye")
	}
	if comparision["compare_time"] > 75:
		speak_engine.say("Now " + time.strftime("%H:%M", time.localtime()))
		speak_engine.runAndWait()
	elif comparision["compare_date"] > 75:
		speak_engine.say("Today " + time.strftime("%d of %b", time.localtime()))
		speak_engine.runAndWait()
	elif comparision["compare_goodbye"] > 75:
		speak_engine.say("Goodbye, sir!")
		speak_engine.runAndWait()
		break
