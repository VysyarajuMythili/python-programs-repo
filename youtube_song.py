import speech_recognition as sr
import pyttsx3
import pywhatkit

def speak(command):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(command)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
            command = r.recognize_google(audio)
            song=command.replace('play','')
            print("playing " + song + "In Youtube")
            speak("play" + song + "In Youtube")
            pywhatkit.playonyt(song)

    except Exception as e:
        print("Problem Occurred", str(e))

takeCommand()
