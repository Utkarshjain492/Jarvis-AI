import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")

    else:
        print("Good Evening Sir")
        speak("Good Evening Sir")