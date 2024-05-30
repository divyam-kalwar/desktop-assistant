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

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Divyam. How are you doing?")
    elif hour>=12 and hour<18:
        speak("Good afternoon Divyam. How are you doing?")
    else:
        speak("Good evening Divyam. How are you doing?")
        
    speak("I am FRIDAY. Tell me Divyam how can I help you?")
    

if __name__ == "__main__":
    while True:
        wish_me()
        
        query = takecommand().lower()
        browser_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences =2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif "youtube" in query:
            speak('Opening Youtube')
            webbrowser.get(using=browser_path).open('youtube.com')
            
        elif "google" in query:
            speak('Opening Google')
            webbrowser.get(using=browser_path).open('google.com')
        
        elif "goodbye" in query:
            exit()