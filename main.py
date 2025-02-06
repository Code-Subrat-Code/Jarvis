import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration = 0.5)
        print("listening",end="",flush=True)
        r.pause_threshold=1.0
        r.phase_threshold=0.3
        r.sample_rate =48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment =2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        # print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)
    try:
        print("\r",end="",flush=True) 
        print("Recognising",end="",flush=True)
        query = r.recognize_google(audio,language ="en-in")
        print("\r",end="",flush=True)
        print(f"User  Said:{query.lower()}\n")
    except Exception as e:
        print("Say that Again:")    
        return("None")
    return query


def cal_day():
    day = datetime.datetime.today().weekday()+1
    day_dict = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"

    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week
def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%S %p")  # Format for current time (HH:MM:SS)
    period = time.strftime("%p")
    print(t)
    day = cal_day()

    if (hour >= 0) and (hour < 12) and (period == 'AM'):
        speak(f"Good Morning, Subrat. It's {day} and the time is {t}")
    elif (hour >= 12) and (hour <= 16) and (period == 'PM'):  
        speak(f"Good Afternoon, Subrat. It's {day} and the time is {t}")
    else:
        speak(f"Good Evening, Subrat. It's {day} and the time is {t}")  
 
def social_media(query):  # Accept query as an argument
    if 'facebook' in query:
        speak("Opening Your Facebook")
        webbrowser.open("https://www.facebook.com")
    elif 'discord' in query:
        speak("Opening Your Discord")
        webbrowser.open("https://www.discord.com")
    elif 'whatsapp' in query:
        speak("Opening Your WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    elif 'instagram' in query:
        speak("Opening Your Instagram")
        webbrowser.open("https://www.instagram.com")
    else:
        speak("I don't recognize this platform.")

def shedule():
    day  = cal_day().lower()
    speak("Boos Today schdule is ")
    week = {
        "Monday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Tuesday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Wednesday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Thursday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Friday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Saturday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class",
        "Sunday":" Boss ,from 10:30 am  to 11:20 am you have software enginerring class , from 11:20 am to 12:10 to Python class"
    }

    if day in week.keys():
        speak(week[day])
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = input("user command-->").lower()  # Convert to lowercase
        if any(platform in query for platform in ["facebook", "discord", "whatsapp", "instagram"]):
            social_media(query)  # Now correctly passing query
        elif("University Time table "in query) or ('shedule' in query):
            shedule()
# # speak("Hello , I am Jarvis")