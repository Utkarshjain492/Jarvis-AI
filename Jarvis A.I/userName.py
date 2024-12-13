import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def getAudio():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say again Sir...")
        speak("Please say again Sir...")
        return "None"
    return query

def rememberName():

    while True:

        print("Sir Do you want me to remember your name?")
        speak("Sir Do you want me to remember your name?")
        print("Listening...")

        query = getAudio()

        if "yes" in query:
            f = open('rememberName.txt', 'r+')
            f.truncate(0)
            f.close()

            print("Ok Sir, I am Listening. Tell me your name Please.")
            speak("Ok Sir, I am Listening. Tell me your name Please.")
            print("Listening...")

            name = getAudio()

            rememberMsg = name.replace("my", "")
            rememberMsg = rememberMsg.replace("remember", "")
            rememberMsg = rememberMsg.replace("jarvis", "")
            rememberMsg = rememberMsg.replace("that", "")
            rememberMsg = rememberMsg.replace("what", "")
            rememberMsg = rememberMsg.replace("said", "")
            rememberMsg = rememberMsg.replace("this", "")
            rememberMsg = rememberMsg.replace("the", "")
            rememberMsg = rememberMsg.replace("name", "")
            rememberMsg = rememberMsg.replace("is", "")
            rememberMsg = rememberMsg.replace("message", "")

            remember = open("rememberName.txt", "a")
            remember.write(rememberMsg)
            remember.close()
            print(f"Ok Sir, Now I will remember that your name is {rememberMsg}.")
            speak(f"Ok Sir, Now I will remember that your name is {rememberMsg}.")
            print(f"Hello {rememberMsg} Sir! Nice to meet you!")
            speak(f"Hello {rememberMsg} Sir! Nice to meet you!")
            break

        elif "no" in query:
            print("Ok Sir, No problem. You can tell me your name I don't remember.")
            speak("Ok Sir, No problem. You can tell me your name I don't remember.")
            print("What is your name Sir?")
            speak("What is your name Sir?")
            print("Listening...")

            name = getAudio()
            name = name.replace("my", "")
            name = name.replace("name", "")
            name = name.replace("is", "")

            print(f"Hello{name} Sir! Nice to meet you!")
            speak(f"Hello{name} Sir! Nice to meet you!")
            breakpoint()

def myName():

    while True:
        print("I don't know your name Sir, You can tell me your name")
        speak("I don't know your name Sir, You can tell me your name")
        print("Do you want to tell me your name?")
        speak("Do you want to tell me your name?")
        print("Listening...")

        query = getAudio()

        if "yes" in query:
            return rememberName()

        elif "no" in query:
            print("Ok Sir, No problem.")
            speak("Ok Sir, No problem.")
            breakpoint()

def remembered():

    while True:
        print("Sir did you tell me your name before?")
        speak("Sir did you tell me your name before?")
        print("Listening...")

        query = getAudio()

        if "yes" in query:
            remember = open("rememberName.txt", "r")
            read = remember.read()
            print("Sir I remembered that your name is " + read)
            speak("Sir I remembered that your name is " + read)
            print("Sir do you want me to clear the memory?")
            speak("Sir do you want me to clear the memory?")
            print("Listening...")

            query = getAudio()

            if "yes" in query:
                print("Ok Sir, I cleared the memory")
                speak("Ok Sir, I cleared the memory")
                f = open('rememberName.txt', 'r+')
                f.truncate(0)
                f.close()
                break

            elif "no" in query:
                print("Ok Sir, I am not clearing the memory.")
                speak("Ok Sir, I am not clearing the memory.")
                break

            else:
                print("Error...")
                return remembered()

        elif "no" in query:
            return rememberName()