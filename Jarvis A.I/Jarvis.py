import os
import pyttsx3
import speech_recognition
import webbrowser
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
chrome = webbrowser.get('chrome')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Hello Sir, My name is Jarvis.")
speak("Hello Sir, My name is Jarvis.")
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        sites = [["open google", "https://www.google.com"], ["open facebook", "https://www.facebook.com/"], ["open youtube", "https://www.youtube.com/"], ["open wikipedia", "https://www.wikipedia.com/"], ["instagram", "https://www.instagram.com/"]]

        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                site[0] = site[0].replace("open", "Opening")
                print(f"Ok Sir, {site[0]} for you.")
                speak(f"Ok Sir, {site[0]} for you.")
                chrome.open(site[1])
                breakpoint()
        if "greet me" in query:
            from GreetMe import greetMe
            greetMe()

        elif "sleep" in query:
            print("Ok Sir, You can call me anytime.")
            speak("Ok Sir, You can call me anytime.")
            break

        elif "i am going" in query:
            print("Ok Sir, You can call me anytime.")
            speak("Ok Sir, You can call me anytime.")
            break

        elif "nothing" in query:
            print("Ok Sir, You can call me anytime.")
            speak("Ok Sir, You can call me anytime.")
            break

        elif "hello" in query:
            remember = open("rememberName.txt", "r")
            read = remember.read()
            print(f"Hello {read} Sir! How are You?")
            speak(f"Hello {read} Sir! How are You?")

        elif "fine" in query:
            print("Nice to hear Sir, How may I help you?")
            speak("Nice to hear Sir, How may I help you?")

        elif "who made you" in query:
            print("Sir Utkarsh Jain made me, He is my God.")
            speak("Sir Utkarsh Jain made me, He is my God.")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {time}")
            speak(f"Sir the time is {time}")

        elif "my name" in query:
            from userName import remembered
            remembered()

        elif "who is your god" in query:
            print("Sir Utkarsh Jain is my god, He made me.")
            speak("Sir Utkarsh Jain is my god, He made me.")

        elif "am your god" in query:
            print("Hello Utkarsh Sir, Nice to meet you Sir.")
            speak("Hello Utkarsh Sir, Nice to meet you Sir.")

        elif "how are you" in query:
            print("I am fine Sir, Thank You for asking")
            speak("I am fine Sir, Thank You for asking")

        elif "thank u" in query:
            print("Your Welcome, Sir")
            speak("Your Welcome, Sir")

        elif "good night" in query:
            print("Good Night Sir, Have a good dreams, You can call me anytime.")
            speak("Good Night Sir, Have a good dreams, You can call me anytime.")
            break

        elif "bye" in query:
            print("Bye Sir, You can call me anytime.")
            speak("Bye Sir, You can call me anytime.")
            break

        elif "your name" in query:
            print("My name is Jarvis, Sir")
            speak("My name is Jarvis, Sir")

        elif "stop" in query:
            print("Ok Sir, You can call me anytime.")
            speak("Ok Sir, You can call me anytime.")
            break

        elif "track 1" in query:
            from music import favourite
            favourite()
            break

        elif "track 2" in query:
            from music import aayi_nai
            aayi_nai()
            break

        elif "track 3" in query:
            from music import badnam
            badnam()
            break

        elif "track 4" in query:
            from music import akhiyan_gulab
            akhiyan_gulab()
            break

        elif "track 5" in query:
            from music import bande_hain_hum_uske
            bande_hain_hum_uske()
            break

        elif "track 6" in query:
            from music import arjan_vailly
            arjan_vailly()
            break

        elif "track 7" in query:
            from music import nature
            nature()
            break

        elif "track 8" in query:
            from music import mujhko_yaad_sataye_teri
            mujhko_yaad_sataye_teri()
            break

        elif "track 9" in query:
            from music import let_music_play
            let_music_play()
            break

        elif "track zero" in query:
            from music import aye_hip_hopper
            aye_hip_hopper()
            break

        elif "google" in query:
            from search import searchGoogle
            searchGoogle(query)
            break

        elif "youtube" in query:
            from search import searchYoutube
            searchYoutube(query)
            break

        elif "wikipedia" in query:
            from search import searchWikipedia
            searchWikipedia(query)
            break

        elif "chrome" in query:
            print("Opening Chrome Sir...")
            speak("Opening Chrome Sir...")
            os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')
            break

        elif "vs" in query:
            print("Opening Visual Studio Code Sir...")
            speak("Opening Visual Studio Code Sir...")
            os.system('"C:/Users/Ujain/AppData/Local/Programs/Microsoft VS Code/Code.exe"')
            break

        elif "pycharm" in query:
            print("Opening PyCharm Sir...")
            speak("Opening PyCharm Sir...")
            os.system('"C:/Program Files/JetBrains/PyCharm 2024.1.6/bin/pycharm64.exe"')
            break

        elif "edge" in query:
            print("Opening Microsoft Edge Sir...")
            speak("Opening Microsoft Edge Sir...")
            os.system('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"')
            break

        elif "desk" in query:
            print("Opening AnyDesk Sir...")
            speak("Opening AnyDesk Sir...")
            os.system('"C:/Program Files (x86)/AnyDesk/AnyDesk.exe"')
            break

        elif "github" in query:
            print("Opening Github Desktop Sir...")
            speak("Opening Github Desktop Sir...")
            os.system('"C:/Users/Ujain/AppData/Local/GitHubDesktop/GitHubDesktop.exe"')
            break

        elif "zoom" in query:
            print("Opening Zoom Sir...")
            speak("Opening Zoom Sir...")
            os.system('"C:/Users/Ujain/AppData/Roaming/Zoom/bin/Zoom.exe"')
            break