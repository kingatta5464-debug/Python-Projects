JARVIS SIMPLE – Voice Assistant

This is a simple Python voice assistant project named Jarvis.
It listens to your voice commands, responds using text-to-speech, and can open popular websites such as Google, YouTube, Facebook, and LinkedIn.

Features

Voice recognition using speech_recognition

Text-to-speech (TTS) using pyttsx3

Opens websites: Google, YouTube, Facebook, LinkedIn

Exit program by saying "stop" or "exit"

Personalized with the name Atta

Requirements

Before running, install the following Python libraries:

pip install speechrecognition pyttsx3
pip install pyaudio


Note: On Windows, if PyAudio fails to install, you may need to download a prebuilt wheel.

How to Run

Clone or download this repository.

Open the folder in terminal/command prompt.

Run the script with:

python main.py

Usage

Say "Jarvis" to activate the assistant.

Example commands:

"open google" → opens Google

"open youtube" → opens YouTube

"open facebook" → opens Facebook

"open linkedin" → opens LinkedIn

Say "stop" or "exit" to quit.

Example Run
Listening...
Recognizing...
You said: jarvis
Yes, What do you want me to do?
Command: open youtube


Jarvis will then respond and open the requested site.

Author

Created by Atta Ul Mustafa