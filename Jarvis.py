import pyttsx3 
import speech_recognition as sr 
import pyaudio
import datetime
import webbrowser
import os
import pywhatkit as wk
import wikipedia
import googlesearch as google
import pyautogui
import cv2
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth



# Initialize the TTS engine  
engine = pyttsx3.init('sapi5')  

# Get available voices  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)  # Use the first voice  

# Set speaking rate (speed)     
engine.setProperty('rate', 170) 

#spotify setting are here
SPOTIPY_CLIENT_ID = "db0efea5b080438f86709fbb97f7fc7d"
SPOTIPY_CLIENT_SECRET = "b96e3b019c6543a18ab8abe59849d615"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))

def play_on_spotify(song):
    results = sp.search(q=song, limit=1)
    
    if results['tracks']['items']:
        song_url = results['tracks']['items'][0]['external_urls']['spotify']
        webbrowser.open(song_url)  # Open song in the default web browser
        print(f"Playing {song} on Spotify...")
    else:
        print("Song not found on Spotify.")



def speak(text):  
    engine.say(text)  
    engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        
    else:
        speak("Good Evening Sir")

    speak(" I Am Jarvis. Please tell me how may I help you today")
        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("Yes Sir")
            speak("Yes Sir")

        elif 'hi' in query:
            print("Hello Sir")
            speak("Hello Sir")

        elif 'type' in query:
            query = takeCommand().lower()
            query = query.replace("type", "")
            pyautogui.typewrite(query, interval=0.1)

        elif 'open notepad' in query:
            speak("Opening Notepad")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif 'close notepad' in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open paint' in query:
            speak("Opening Paint")
            ppath = "C:\\Windows\\System32\\mspaint.exe"
            os.startfile(ppath)
        elif 'close paint' in query:
            speak("Closing Paint")
            os.system("taskkill /f /im mspaint.exe")

        elif 'open command prompt' in query:
            speak("Opening Command Prompt")
            os.system("start cmd")

        elif 'how are you' in query:
            speak('Hey, I am fine Thanks for asking, How may i help you Sir?')

        elif 'my name' in query:
            print("Nayak Rachan")
            speak("Nayak Rachan")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        
        elif 'leetcode' in query or 'lead' in query:
            speak("opening Leetcode")
            print("Opening Leetcode")
            webbrowser.open("https://leetcode.com/")

        elif 'chat gpt' in query:
            speak("Opening ChatGPT")
            print("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com/")

        
        elif "who are you" in query:
            print("My am Jarvis, an AI assistant")
            speak("My am Jarvis, an AI assistant")
            print("I can do the things my programmer trained me to do")
            speak("I can do the things my programmer trained me to do")

        elif "who created you" in query:
            print("I was created by my Master Rachan")
            speak("I was created by my Master Rachan")

        elif "just open youtube" in query:
            webbrowser.open("youtube.com")

        elif "just open google" in query:
            webbrowser.open("google.com")

        elif "who is" in query:
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)

        elif "what is" in query:
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)

        elif "spotify" in query:
            song = query.replace("play","").strip()
            play_on_spotify(song)

        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song}")
            wk.playonyt(song)

        elif 'open google' in query:
            speak("What do you wanna know here")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")
            results = google.summary(query, sentence  = 1)
            speak(results)

        elif "open youtube" in query:
            speak("What would you love to watch here")
            query = takeCommand().lower()
            wk.playonyt(f'{query}')

        elif 'search on youtube' in query:
            query = query.replace('search on youtube'," ")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'close youtube' in query:
            os.system("taskkill/f /im youtube.exe")

        elif 'open camera' in query:
            speak("Opening Camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'take a screenshot' in query:
            speak("tell me name of the file")
            name = takeCommand().lower()
            time.sleep(2)
            screenshot = pyautogui.screenshot()
            screenshot.save("C:\\Users\\Rachan\\Desktop\\screenshot.png")
            speak("Screenshot taken")

        elif('open calculator') in query:
            speak("Opening Calculator")
            os.system("calc")

        elif 'shut down' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")
        elif 'restart' in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")
        elif 'sleep' in query:
            speak("Sleeping the system")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        elif 'close browser' in query:
            os.system("taskkill/f /im chrome.exe")

        elif 'thank you' in query:
            speak("Welcome Sir")

        

        elif 'exit' in query:
            speak("Goodbye Sir, Have a great day")
            exit()

        