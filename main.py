import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser

# Initialize Text-to-Speech Engine Once (Optimized)
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', engine.getProperty('rate') - 50)
engine.setProperty('volume', engine.getProperty('volume') + 0.25)

# Speak Function
def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Function
def command():
    """Listen for a voice command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("🎤 Listening...")
        r.pause_threshold = 1.0
        r.dynamic_energy_threshold = True
        r.energy_threshold = 1000  # Adjusted for better accuracy
        r.phrase_time_limit = 10
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"🗣 User Said: {query.lower()}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("🤷 Sorry, I didn't catch that. Please repeat.")
            return "none"
        except sr.RequestError:
            print("🌐 Network error. Please check your internet connection.")
            return "none"

# Get Current Day
def cal_day():
    day_dict = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 
        3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"
    }
    day_of_week = day_dict[datetime.datetime.today().weekday()]
    print(f"📅 Today is {day_of_week}")
    return day_of_week

# Greet the User
def wishMe():
    hour = datetime.datetime.now().hour
    t = time.strftime("%I:%M %p")
    day = cal_day()
    
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    speak(f"{greeting}, Subrat. Today is {day}, and the time is {t}.")

# Open Social Media
def social_media(query):
    platforms = {
        "facebook": "https://www.facebook.com",
        "discord": "https://www.discord.com",
        "whatsapp": "https://web.whatsapp.com",
        "instagram": "https://www.instagram.com"
    }
    
    for platform in platforms:
        if platform in query:
            speak(f"Opening Your {platform.capitalize()}")
            webbrowser.open(platforms[platform])
            return

    speak("I don't recognize this platform.")

# User Schedule
def schedule():
    day = cal_day()
    schedule_dict = {
        "Monday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Tuesday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Wednesday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Thursday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Friday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Saturday": "Boss, from 10:30 AM to 11:20 AM you have Software Engineering, then from 11:20 AM to 12:10 PM, Python class.",
        "Sunday": "Boss, you have no classes today. Enjoy your day!"
    }
    
    speak("Boss, today's schedule is:")
    speak(schedule_dict.get(day, "No schedule available."))

# Main Function
if __name__ == "__main__":
    speak("Hello, I am Jarvis.")
    wishMe()

    while True:
        print("\n🔹 Type a command or press ENTER to speak...")
        query = input("User Command --> ").strip().lower()  # Accept user input

        if query == "":  # If user presses ENTER, switch to voice input
            query = command()

        if query in ["exit", "stop", "quit"]:
            speak("Goodbye, Boss!")
            break
        elif any(platform in query for platform in ["facebook", "discord", "whatsapp", "instagram"]):
            social_media(query)
        elif "schedule" in query or "timetable" in query:
            schedule()
        else:
            speak("Sorry, I didn't understand that.")
