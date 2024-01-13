#!/usr/bin/env python3
#
# Build RaspberryPi chatbot with OpenAI assistants api - Similar to smart speaker
#
# Python program to translate speech to text, Google to recognize audio and ask 
# OpenAI assistants api a question. After reponse has been requested, verbally respond with the answer.
# Install the packages and start asking questions on your linux machine
# Remember to install required packages, add api key, and name of AI
# 
#
# Sources
# https://github.com/daveebbelaar/python-whatsapp-bot/blob/main/start/assistants_quickstart.py
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#
# INSTALL !add more if needed
# pip3 install speechrecognition pyttsx3 openai pandas pyfiglet
# sudo apt install espeak jackd2 python3-pyaudio flac
#
# Be sure to restart RaspberryPi
#
# import these libraries, may have to use pip3 install for many of them (above command)

import speech_recognition as sr, sys, pyttsx3, pandas as pd, warnings, pyfiglet
from colorama import Fore
warnings.filterwarnings('ignore')
from openai import OpenAI
import shelve
import os
import time

# input environment variable here for OPENAI API Key
OPEN_AI_API_KEY = os.getenv("OKEY")
client = OpenAI(api_key=OPEN_AI_API_KEY)
# Initialize the recognizer
r = sr.Recognizer()
wa_id = "777"

# --------------------------------------------------------------
# Upload file
# --------------------------------------------------------------
def upload_file(path):
	# Upload a file with an "assistants" purpose
	file = client.files.create(file=open(path, "rb"), purpose="assistants")
	return file


file = upload_file("/home/picar/picar.txt")


# --------------------------------------------------------------
# Create assistant
# --------------------------------------------------------------
def create_assistant(file):
	"""
	You currently cannot set the temperature for Assistant via the API.
	"""
	assistant = client.beta.assistants.create(
		name="Picar Assistant",
		instructions="You're a helpful Picar assistant that can assist users with questions. \
		You're also a robot, remote controlled car powered by a raspberry pi. Use your knowledge \
		base to best respond to user queries. If you don't know the answer, say simply that you \
		cannot help with question and advise the user to try researching the web. Be friendly \
		and funny. Be brief in your responses to only 2 sentences or less.",
		tools=[{"type": "retrieval"}],
		model="gpt-4-1106-preview",
		file_ids=[file.id],
	)
	return assistant


assistant = create_assistant(file)

# --------------------------------------------------------------
# Thread management
# --------------------------------------------------------------
def check_if_thread_exists(wa_id):
	with shelve.open("threads_db") as threads_shelf:
		return threads_shelf.get(wa_id, None)


def store_thread(wa_id, thread_id):
	with shelve.open("threads_db", writeback=True) as threads_shelf:
		threads_shelf[wa_id] = thread_id


# --------------------------------------------------------------
# Generate response
# --------------------------------------------------------------
def generate_response(message_body, wa_id, name):
	# Check if there is already a thread_id for the wa_id
	thread_id = check_if_thread_exists(wa_id)

	# If a thread doesn't exist, create one and store it
	if thread_id is None:
		print(f"Creating new thread for {name} with wa_id {wa_id}")
		thread = client.beta.threads.create()
		store_thread(wa_id, thread.id)
		thread_id = thread.id

	# Otherwise, retrieve the existing thread
	else:
		print(f"Retrieving existing thread for {name} with wa_id {wa_id}")
		thread = client.beta.threads.retrieve(thread_id)

	# Add message to thread
	message = client.beta.threads.messages.create(
		thread_id=thread_id,
		role="user",
		content=message_body,
	)

	# Run the assistant and get the new message
	new_message = run_assistant(thread)
	return new_message


# --------------------------------------------------------------
# Run assistant
# --------------------------------------------------------------
def run_assistant(thread):
	# Retrieve the Assistant
	assistant = client.beta.assistants.retrieve("asst_pVQuThzCKzB70WPMJdpHnCe")

	# Run the assistant
	run = client.beta.threads.runs.create(
		thread_id=thread.id,
		assistant_id=assistant.id,
	)

	# Wait for completion
	while run.status != "completed":
		# Be nice to the API
		time.sleep(0.5)
		run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

	# Retrieve the Messages
	messages = client.beta.threads.messages.list(thread_id=thread.id)
	new_message = messages.data[0].content[0].text.value
	return new_message

# --------------------------------------------------------------
# speech to text text to speech
# --------------------------------------------------------------

# Function to convert text to
# speech
def SpeakText(command):
	 
	# Initialize the engine
	engine = pyttsx3.init()
	engine.setProperty('rate', 140)
	engine.say(command)
	engine.runAndWait()

# Opening art
def art():

	ascii_banner = pyfiglet.figlet_format("PICAR A.I.\n")
	print(Fore.CYAN + ascii_banner)

# introduction function
def milliDollarQuestion():    

	ask = "Hello! This is Pie Car. What would you like to ask?"
	print('')
	print('')
	print(Fore.MAGENTA + ask + "\n")
	SpeakText(ask)

# Loops waiting for the keyword jarvis then asks chatgpt your question utilizing google trans. and
# responds
def main(r):
	# yay art
	art()
	milliDollarQuestion()
	# Loops waiting for the request then asks chatgpt your question utilizing google trans. and
	# responds
	while(1):   
		# Exception handling to handle
		# exceptions at the runtime
		try:
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				 
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level
				r.adjust_for_ambient_noise(source2, duration=0.2)
				 
				# listens for the user's input
				audio2 = r.listen(source2)
				 
				# Using google to recognize audio
				MyText1 = r.recognize_google(audio2)
				MyText = MyText1.lower()
				response = generate_response(MyText,wa_id, "Bennett")
				print('')
				print('')
				# if you hear these exit the program
				if "exit" in str(MyText) or "bye" in str(MyText) or "sleep" in str(MyText):
					SpeakText("Ok bye. Have a goodin!")
					exit()
				# reference for what was asked
				print(Fore.RED + "Did you ask ",MyText)
				print('')
				print('')
				# print response from chatgpt
				print(Fore.YELLOW + response)
				# now speak it
				SpeakText(response)
				print('')
				print('')
				 
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			 
		except sr.UnknownValueError:
			print("unknown error occurred\n")
# --------------------------------------------------------------
# Test assistant
# --------------------------------------------------------------

if __name__ == "__main__":
	main(r)
