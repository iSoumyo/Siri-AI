import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning !")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    elif hour>=18 and hour<21:
        speak("Good evening ")    
            
    elif hour>=21 and hour<22:
        speak("Good night !")

    speak(" i am ,siri,,,,  Plese tell me how can I help you") 

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
                     
def takeCommand():     
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source) 

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query    

     
if __name__ == "__main__":
    wishme()
    #while True: 
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia..", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
          speak("opening youtube")
          webbrowser.open("https://youtube.com")
          speak("now you can go")
        elif 'google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")
            speak("now you can go")    

        elif 'gmail' in query:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com//#path")  

        elif 'earth' in query:
            webbrowser.open("https:\\earth.google.com\\web\\@58.85285343,97.60760663,-228.59089833a,2120203.21063757d,90y,217.12865799h,0t,0r")

        elif 'hey siri' in query:
            speak("Hello mr.#your name, i am listening")             

        elif 'music' in query:
            music_dir = 'C:\\#path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs(11)))

        elif 'to disco' in query: #sample songs
            Path="https:\\www.youtube.com\\watch?v=M03GOY5eINg&list=RDMMDwUgoUhgzLo&index=2"
            os.startfile(Path)  

        elif 'you are my sonia' in query: #sample songs
            Path="https:\\www.youtube.com\\watch?v=DwUgoUhgzLo&list=RDMMDwUgoUhgzLo&index=1"  
            os.startfile(Path)   

      

        elif 'visual studio' in query:
            speak("opening visqual studio code")
            codePath="C:\\#your path"
            os.startfile(codePath)     

        elif 'zoom' in query:
            speak("Opening zoom")
            Path="C:\\#your path"
            os.startfile(Path)

        elif 'chrome' in query:
            Path="C:\\#your path"
            os.startfile(Path) 
            speak("Now you can go, with chrome")       
  

        elif 'machayenge' in query:
            speak("playing machayenge") #sample songs
            Path="https:\\www.youtube.com\\watch?v=8ZHIkihVPjo&list=RD8ZHIkihVPjo&start_radio=1" 
            os.startfile(Path)  
        
        elif 'yalgaar' in query:
            speak("playing yalgaar") #sample songs
            Path="https:\\www.youtube.com\\watch?v=zzwRbKI2pn4"
            os.startfile(Path)

        elif 'office exam on vaccine' in query:
            speak("office exam on vaccine") #sample video
            Path="https:\\www.youtube.com\\watch?v=Zr3PukaVXFo"  
            os.startfile(Path)  

        elif 'love you' in query:
            speak("Thank you sir") 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}") 

        elif 'hai' in query:
            speak("hello sir")

        elif 'how are you' in query:
            speak("I am good,what about you?")   

       
        elif "despacito" in query:
            speak("playing despacito") #sample songs
            Path="https:\\www.youtube.com\\watch?v=5TJqoxsoXc4&list=RDMM5TJqoxsoXc4&index=1"
            os.startfile(Path)

      
       

        elif 'happy birthday' in query:
            speak("Happy birthday, many many happy, returns of the day")
            Path="https:\\www.youtube.com\\watch?v=bV2GklFBaT8" 
            os.startfile(Path)  

        elif 'choclate' in query:
            speak("playing choclate") #sample songs
            Path="https:\\www.youtube.com\\watch?v=HARdHQb1Li4&list=RDHARdHQb1Li4&index=1"
            os.startfile(Path)


        elif 'date' in query:
            speak("the current date is")
            date()   

        

        elif 'joker' in query:
            speak("playing joker bgm") #sample songs
            Path="https:\\www.youtube.com\\watch?v=YKLX3QbKBg0&list=RDYKLX3QbKBg0&start_radio=1&ab_channel=BASSBOOSTEDSONGS"    
            os.startfile(Path)

        elif 'when is your birthday' in query:
            speak("My creator created me on twenty seventh october ,so it's my birthday ")  
     

        elif 'thank you' in query:
            speak("welcome Sir,always at your service")
            print(speak)

       
        elif 'good afternoon' in query:
            speak("Good afternoon Sir")

        elif 'wishme' in query:
            speak("good morning Mr sen")
