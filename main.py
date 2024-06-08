import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

dict1 = {
    "David": "amanbariar22@gmail.com"
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi! I am Jarvis .  How May I Help You")


def takecommand():
    # It takes microphone input from the user and return string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='eng-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print("Say That Again Please....")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abrgamer22@gmail.com', 'ABRgamer@2222')
    server.sendmail("abrgamer22@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while (True):
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'play my songs' in query:
            music_dir = 'G:\\Recordings'
            songs = os.listdir(music_dir)
            d = random.choice(songs)
            os.startfile(os.path.join(music_dir, d))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"the time is : {strTime}")
            speak(f"the time is : {strTime}")

        elif 'date' in query:
            x = datetime.datetime.now()
            date = x.strftime("%d %b %Y")
            day = x.strftime("%A")
            print(date)
            print(day)
            speak(f"Its : {date}")
            speak(f" {day} ")

        elif 'open pycharm' in query:
            codePath = "D:\\Pycharm\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64"
            os.startfile(codePath)

        elif 'open code' in query:
            e = "C:\\Users\\Aman Bariar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(e)

        elif 'send email to' in query:
            try:
                speak("What Should I Say?")
                content = takecommand()
                to = dict1["David"]
                sendEmail(to, content)
                speak("Email Has Been Sent!")

            except Exception as e:
                print(e)
                speak("Sorry. I am Not Able to the Send this Email")

        elif 'play song' in query:
            query = query.replace('play song', '')
            result = query
            speak("Playing song..." + result)
            pywhatkit.playonyt(result)

        elif 'introduce' in query:
            speak("I am Jarvis Made by Mister Aman Bariar . My Work Is To Help Aman & Make His Work Easy")

        elif 'how old are you' in query:
            speak(" I Don't Know That ")

        elif 'actor' in query:
            speak("My Favourite Actor Is Shah Rukh Khan")

        elif 'actress' in query:
            speak("My Favourite Actress Is Kiara Advani")

        elif 'cricketer' in query:
            speak(" Rohit Sharma ")

        elif 'anime' in query:
            speak(" Dragon Ball ")

        elif 'sport' in query:
            speak("My Favourite Sport is Cricket")

        elif 'food' in query:
            speak("pizza")

        elif 'movie' in query:
            speak("My Favourite Movie Is D D L J ")

        elif 'web series' in query:
            speak("My Favourite Web Series is Game of Thrones")

        elif 'singer' in query:
            speak("My Favourite Singer is Atif Aslam & Shreya Goshal")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'give information about' in query:
            query = query.replace('give information about', '')
            info = query
            speak("Giving information about.." + info)
            pywhatkit.info(info, lines=3)

        elif 'stop' in query:
            speak("Thank You! Call Me Again if You Need Help")
            break

