import os
import webbrowser
import pyttsx3

engine = pyttsx3.init()
engine.runAndWait()
print("")
print("\n 1.GOOGLE CHROME \n 2.NOTEPAD\n 3.FOR EXIT")
print("\n  ============================================ Welcome To Application menu ============================================")
pyttsx3.speak("select the option which you want to open")

while True:
    input_string = input()
    input_string=input_string.upper()
    if ("DONT" in input_string) or ("DON'T" in input_string) or ("NOT" in input_string):
        pyttsx3.speak("Type Again")
        continue
    elif ("GOOGLE" in input_string) or ("SEARCH" in input_string) or ("WEB BROWSER" in input_string) or ("CHROME" in input_string) or ("BROWSER" in input_string) or ("1" in input_string):
        pyttsx3.speak("Opening")
        pyttsx3.speak("GOOGLE CHROME")
        print(".")
        url = 'http://docs.python.org/'
        chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chromedir).open(url)
    elif ("NOTE" in input_string) or ("NOTES" in input_string) or ("NOTEPAD" in input_string) or ("EDITOR" in input_string) or ("2" in input_string):
        pyttsx3.speak("Opening")
        pyttsx3.speak("NOTEPAD")
        print(".")
        os.system("Notepad")
    elif ("EXIT" in input_string) or ("QUIT" in input_string) or ("CLOSE" in input_string) or ("3" in input_string):
        pyttsx3.speak("Exiting")
        break
 
    # for invalid input
    else:
        pyttsx3.speak(input_string)
        pyttsx3.speak("is Invalid,Please try again")
        print(".")