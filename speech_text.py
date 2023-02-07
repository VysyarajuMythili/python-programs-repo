import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    print("say something")
    audio=r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))