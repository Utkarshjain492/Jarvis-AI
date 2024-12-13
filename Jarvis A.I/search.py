import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

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

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Recognizing...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Searching...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Results...")
        return "None"
    return query

query = takeCommand().lower()

def searchGoogle(query):
    if 'google' in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google", "")
        query = query.replace("search", "")
        query = query.replace("from", "")

        print("Searching from Google...")
        speak("Searching from Google...")
        print("Here what I found, Sir.")
        speak("Here what I found, Sir.")

    try:
        pywhatkit.search(query)

    except:
        print("Done Sir!")
def searchYoutube(query):
    if 'youtube' in query:
        speak("Searching from YouTube...")

        query = query.replace("search", "")
        query = query.replace("jarvis", "")
        query = query.replace("youtube", "")
        query = query.replace("from", "")
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + query)

        print("Here what I found, Sir.")
        speak("Here what I found, Sir.")

def searchWikipedia(query):
    if 'wikipedia' in query:
        speak("Searching from Wikipedia...")

        query = query.replace("search", "")
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia", "")
        query = query.replace("tell me", "")
        query = query.replace("about", "")
        query = query.replace("from", "")
        results = wikipedia.summary(query, sentences = 20)
        print("Here what I found, Sir. According to Wikipedia...")
        speak("Here what I found, Sir. According to Wikipedia...")
        print(results)
        speak(results)