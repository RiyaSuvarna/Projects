import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Riya!")
    else:
        speak("Welcome Back Riya!")
        speak("How may I help you Riya!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"You said: {query}\n")
        speak("Cool, I'm on it.")
        speak("Just a second .")
       
    except Exception as e:
        print(e)
        speak("Sorry, Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music\\kp'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Riya, the time is {strTime}")

        elif 'open image' in query:
            codePath = "C:\\Users\\hp\\Pictures\\Moon.png"
            os.startfile(codePath)


        elif "bye" in query:
            speak("Bye Riya")
            exit()
