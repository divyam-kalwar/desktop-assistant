import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# print(type(voices))
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

# Speak function
def speak(text):
    '''This function take text input 
    and return it in audio'''
    engine.say(text)
    engine.runAndWait()

def takecommand():
    ''' This function will recognize voice 
    and return it in text'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
text = takecommand()
speak(text)