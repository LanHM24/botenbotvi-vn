import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
from gtts import gTTS

LanCongChua=pyttsx3.init()
voice=LanCongChua.getProperty('voices')
LanCongChua.setProperty('voice',voice[0].id)

def speak(audio):
    print('Lan công chúa: ' + audio)
    LanCongChua.say(audio)
    LanCongChua.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning my Princess")
    elif hour >=12 and hour<18:
        speak("Good afternoon my Princess")
    elif hour >=18 and hour<24:
        speak("Good night my Princess")
    speak("how can I help you")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        query = c.recognize_google(audio,language='en')
        print("Hà Mai Lan: "+ query )
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query

if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        
        elif "quit" in query:
            speak("OK. Goodbye my love. Call me when u need")
            quit()

        elif "thanks" in query:
            speak("OK. Goodbye my love. Call me when u need")
            quit()

        elif 'time' in query:
            time()