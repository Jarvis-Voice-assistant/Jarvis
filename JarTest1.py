import os
import sys
import time
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz

#Логика
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
	"compare_goodbye" : fuzz.token_set_ratio(query.lower(), "goodbye"),
	"compare_music" : {
		"jackpot" : fuzz.token_set_ratio(query.lower(), "jackpot"),
		"toss_to_the_witcher" : fuzz.token_set_ratio(query.lower(), "toss to the witcher"),
		"falling" : fuzz.token_set_ratio(query.lower(), "falling"),
		"look_at_me_now" : fuzz.token_set_ratio(query.lower(), "look at me now"),
		"roses" : fuzz.token_set_ratio(query.lower(), "roses"),
		"hills" : fuzz.token_set_ratio(query.lower(), "hills"),
		"immigrant_song" : fuzz.token_set_ratio(query.lower(), "immigrant song"),
		"back_in_black" : fuzz.token_set_ratio(query.lower(), "back in black"),
		"old_town_road" : fuzz.token_set_ratio(query.lower(), "old town road")
		},
	"compare_telegram" : fuzz.token_set_ratio(query.lower(), "telegram")
	}
	if comparision["compare_time"] > 75:
		speak_engine.say("Now " + time.strftime("%H:%M", time.localtime()))
		speak_engine.runAndWait()
	elif comparision["compare_date"] > 75:
		speak_engine.say("Today " + time.strftime("%d of %b", time.localtime()))
		speak_engine.runAndWait()
	elif comparision["compare_music"]["jackpot"] > 75:
		os.system("/music/jackpot.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["toss_to_the_witcher"] > 75:
		os.system("/music/toss_to_the_witcher.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["falling"] > 75:
		os.system("/music/falling.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["look_at_me_now"] > 75:
		os.system("/music/look_at_me_now.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["roses"] > 75:
		os.system("/music/roses.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["hills"] > 75:
		os.system("/music/hills.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["immigrant_song"] > 75:
		os.system("/music/immigrant_song.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["back_in_black"] > 75:
		os.system("/music/back_in_black.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_music"]["old_town_road"] > 75:
		os.system("/music/old_town_road.mp3")
		speak_engine.runAndWait()
	elif comparision["compare_goodbye"] > 75:
		speak_engine.say("Goodbye, sir!")
		speak_engine.runAndWait()
		break
