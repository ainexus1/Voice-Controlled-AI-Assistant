import pyttsx3
import datetime
import speech_recognition
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    Year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().date)
    speak("The current date is")
    speak(Year)
    speak(month)
    speak(date)

def wishme():
    speak("Welcome")
    time()
    date()

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning sir")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")   
    else:
        speak("Good Night sir") 

    speak("Jarvis at your service. How can I assist you today?")

wishme()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please....")

        return "None"
    return query  

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '123') #add your email here
    server.sendmail('') #add receiver's email here 
    server.close() 

def screenshot():
    img = pyautogui.screenshot()
    img.save("") #add the path to save image

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery Percentage is")
    speak(battery.percent)    

if __name__ == "__main__":
    wishme()
    while True:

        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()  
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence=2)    
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?") 
                content = takeCommand()
                to = '' #receiver's email here 
                sendemail(to, content)
                speak("Email has been successfully sent")

            except Exception as e:
                print(e)
                speak("unable to send email")
        elif 'search in chrome' in query:
            speak("What should I search")
            chromepath = '%s' #location of chrome.exe
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:    
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")   

        elif 'play songs' in query:
            songs_dir = '' #add your music directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))   

        elif 'remember that' in query:
            speak("what should I remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()  

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())  

        elif 'screenshot' in query:
            screenshot()
            speak("Done")    

        elif 'cpu' in query:
            cpu()              

        elif 'offline' in query:
            quit()