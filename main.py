import pyttsx3
import speech_recognition
from datetime import date, datetime

# Step Initial
robot_ear = speech_recognition.Recognizer()
robot = pyttsx3.init()

# Setting voice and speed rate
voices = robot.getProperty('voices') 
robot.setProperty('voice', voices[1].id) 

rate = robot.getProperty('rate')  
robot.setProperty('rate', 135)


while True:
    with speech_recognition.Microphone() as mic:
        print("Jira: I'm Listening...")
        audio = robot_ear.listen(mic)
    print("Jira: ...")
    try:
        you_said = robot_ear.recognize_google(audio)
    except:
        you_said = "Jira: Sorry! I dit not hear what you said, try again!"

    print("You: " + you_said)

    if you_said == "":
        robot_brain = "Sorry! I can't hear you, try again!"
    elif "hello" in you_said or "hi" in you_said:
        robot_brain = "Hello! I am Jira. I'm the Virtual Assistant of Bacdong."
    elif "today" in you_said:
        today = date.today()
        current_date = today.strftime("%B %d, %Y")
        robot_brain = current_date
    elif "time" in you_said:
        now = datetime.now()
        current_time = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you_said:
        robot_brain = "Ah! It's Mr.Donald Trump!"
    elif "bye" in you_said or "goodbye" in you_said:
        robot_brain = "Bye! Have a good day!"
        robot.say(robot_brain)
        robot.runAndWait()
        break
    else:
        robot_brain = "Jira: Sorry! I dit not hear what you said, try again!"

    print("Jira: " + robot_brain)

robot.say(robot_brain)
robot.runAndWait()