import pyttsx3 
import datetime
import speech_recognition as sr  
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil   
import pyjokes 
import requests
#text to speech conversion  library 
#pip install speechrecognition
#pip install wikipedia
#pip install pyautogui
#pip install psutil
#pip install pyjokes
#pip install requests
engine = pyttsx3.init()


def speak(audio):

    print("Jarvis:", audio)
    engine.say(audio) 
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak("the current time is")
    speak(Time)
# speak("current time is",)
# time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
# speak("the current date is")    
# date()


def wishes():
    hour = datetime.datetime.now().hour
    if (hour>=6 and hour<12):
      speak("Good morning sir")
    elif(hour>=12 and hour<17):
       speak("Good afternoon sir")
    elif(hour>=17 and hour<21):
       speak("Good evening sir")
    else:
     speak("Good night sir")
    speak("welcome back")
    # speak("the current time is")
    # time()
    # speak("the current date is")
    # # date()
    
    speak("This is Jarvis assistant is at your service. please tell me how can i help you")

# wishes()


def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
     print("Listening......")
     r.pause_threshold = 1
     audio = r.listen(source)
     try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(query)
     except Exception as e:
            print(e)
            speak("say that again please.")
            return "none"
     return query       

# takeCommand()     

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abc@gmail.com','App_password') #to get app password, go to your secuity page of gmail then select app password, type mail and generate then it will provide a password
    server.sendmail('abc@gmail.com',to,content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\file\\OneDrive\\Documents\\python\\ss.jpg')#copy path the folder where your photo has to be stored


def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
def battery():    
    battery = psutil.sensors_battery()
    speak('battery percentage is at')
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())


def getWeather(city):
    api_key = "Weatherbit API key"  # Your Weatherbit API key, go to website weatherbit and create api keys and paste here
    base_url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}&units=M"
    
    # Make the API request
    response = requests.get(base_url)
    data = response.json()

    print("Full API Response:")
    print(data)  # Print the entire response for debugging

    # Check if the request was successful
    if response.status_code == 200:
        if "data" in data and len(data["data"]) > 0:
            weather = data["data"][0]
            weather_desc = weather["weather"]["description"]
            temp = weather["temp"]

            # Create and speak the weather report
            weather_report = f"The temperature in {city} is {temp} degrees Celsius with {weather_desc}."
            speak(weather_report)
        else:
            speak(f"Error fetching weather data: No data found for {city}.")
    else:
        error_message = data.get('error', 'Unknown error')
        speak(f"Error fetching weather data: {error_message}")


if __name__ == "__main__":
    wishes()
    while True:
        query = takeCommand().lower()


        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif'wikipedia' in query:
            speak("searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'email' in query:
            try:
                speak("what should be the content: ")
                content = takeCommand()
                to = 'abcd@gmail.com'
                sendEmail(to,content)
                speak("Email have been successfully sent")
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'search' in query:
            speak("what should i search:")
            # chromepath = "C:/Program Files/Mozilla Firefox/firefox.exe"
            search = takeCommand().lower()
            # wb.get(chromepath).open_new_tab('https://www.' + search + '.com')
            wb.open_new_tab('https://www.' + search + '.com')

        elif'logout' in query:
            os.system("shutdown -l")    

        elif'shutdown' in query:
            os.system("shutdown /s /t l")    

        elif'restart' in query:
            os.system("shutdown /r /t l")   

        elif 'play songs' in query:
            songs_dir = 'C:\\Users\\music1\\Music\\Songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[10]))
        elif 'remember' in query:
            speak("what should i remember:")
            data = takeCommand()
            speak("you said me to remember is"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")  

        elif 'cpu' in query:
            cpu()

        elif 'battery' in query:
            battery()   
        elif 'jokes' in query:
            jokes()   

        elif 'weather' in query:
            speak("Please tell me the city name.")
            city = takeCommand().lower()
            getWeather(city)    
 
        elif 'Bye' in query:
            speak("Bye sir")
            quit()   
            