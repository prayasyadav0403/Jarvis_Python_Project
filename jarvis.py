import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Prayas. please tell me How can i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prayassushan@gmail.com', '@Jojo0409')
    server.sendmail('prayassushan@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
     # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'open bing' in query:
            webbrowser.open("bing.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open niti aayog' in query:
            webbrowser.open("niti.gov.in")

        elif 'open pib' in query:
            webbrowser.open("pib.nic.in")

        elif 'open newsonair' in query:
            webbrowser.open("newsonair.nic.in")

        elif 'open w3schools' in query:
            webbrowser.open("w3schools.com")

        elif 'open python' in query:
            webbrowser.open("python.com")

        elif 'play music' in query:
            music_dir = "E:\MY MUSIC\BOLLYWOOD SLOW"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[17]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Prayas, the time is {strTime}")

        elif 'open visual code' in query:
            Path = "C:\\Users\\india\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        elif 'open chrome' in query:
            Path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Path)

        elif 'open pycharm' in query:
            Path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(Path)

        elif 'open cisco' in query:
            Path = "C:\\Program Files (x86)\\Cisco Packet Tracer 6.2sv\\bin\\PacketTracer6.exe"
            os.startfile(Path)

        elif 'email to prayas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prayassushan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend prayas. I am not able to send this email")
