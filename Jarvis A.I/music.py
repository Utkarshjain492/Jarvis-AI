import pyttsx3
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def favourite():
    print("Ok Sir, Playing audio track 1 favourite from music.")
    speak("Ok Sir, Playing audio track 1 favourite from music.")
    musicPath = '"Music/Favourite.mp3"'
    os.system(f"{musicPath}")

def aayi_nai():
    print("Ok Sir, Playing audio track 2 Aayi Nai from music.")
    speak("Ok Sir, Playing audio track 2 Aayi Nai from music.")
    musicPath = '"Music/Aayi Nai.mp3"'
    os.system(f"{musicPath}")

def badnam():
    print("Ok Sir, Playing audio track 3 Badnam from music.")
    speak("Ok Sir, Playing audio track 3 Badnam from music.")
    musicPath = '"Music/Badnam.mp3"'
    os.system(f"{musicPath}")

def akhiyan_gulab():
    print("Ok Sir, Playing audio track 4 Akhiyan Gulab from music.")
    speak("Ok Sir, Playing audio track 4 Akhiyan Gulab from music.")
    musicPath = '"Music/Akhiyan Gulab.mp3"'
    os.system(f"{musicPath}")

def bande_hain_hum_uske():
    print("Ok Sir, Playing audio track 5 Bande Hain Hum Uske from music.")
    speak("Ok Sir, Playing audio track 5 Bande Hain Hum Uske from music.")
    musicPath = '"Music/Bande Hain Hum Uske.mp3"'
    os.system(f"{musicPath}")

def arjan_vailly():
    print("Ok Sir, Playing audio track 6 Arjan Vailly from music.")
    speak("Ok Sir, Playing audio track 6 Arjan Vailly from music.")
    musicPath = '"Music/Arjan Vailly.mp3"'
    os.system(f"{musicPath}")

def nature():
    print("Ok Sir, Playing audio track 7 Nature from music.")
    speak("Ok Sir, Playing audio track 7 Nature from music.")
    musicPath = '"Music/Nature.mp3"'
    os.system(f"{musicPath}")

def mujhko_yaad_sataye_teri():
    print("Ok Sir, Playing audio track 8 Mujhko Yaad Sataye Teri from music.")
    speak("Ok Sir, Playing audio track 8 MUjhko Yaad Sataye Teri from music.")
    musicPath = '"Music/Mujhko Yaad Sataye Teri.mp3"'
    os.system(f"{musicPath}")

def let_music_play():
    print("Ok Sir, Playing audio track 9 Let the music play from music.")
    speak("Ok Sir, Playing audio track 9 Let the music play from music.")
    musicPath = '"Music/Let The Music Play.mp3"'
    os.system(f"{musicPath}")

def aye_hip_hopper():
    print("Ok Sir, Playing audio track 0 Aye Hip Hopper from music.")
    speak("Ok Sir, Playing audio track 0 Aye Hip Hopper from music.")
    musicPath = '"Music/Aye Hip Hopper.mp3"'
    os.system(f"{musicPath}")