import pyttsx3
import speech_recognition
from datetime import date, datetime
# from say import say

robot = pyttsx3.init()
voices = robot.getProperty('voices') 
robot.setProperty('voice', voices[1].id) 

rate = robot.getProperty('rate')  
robot.setProperty('rate', 135)



robot_brain = ""
you_said = "hello"

print("You: " + you_said)

if you_said == "":
    robot_brain = "Sorry! I can't hear you, try again!"
elif "hello"in you_said:
    robot_brain = "Hello! I am Jira. I'm the Virtual Assistant of Bacdong."
elif "today" in you_said:
    today = date.today()
    robot_brain = today.strftime("%B %d, %Y")
elif "time" in you_said:
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes %S seconds")
elif "president" in you_said:
    robot_brain = "Ah! It's Mr.Donald Trump!"
elif "goodbye" in you_said:
    robot_brain = "Bye! Have a good day!"
    print("Jira: " + robot_brain)
else:
    robot_brain = "I'm fine, thank you and you."

print("Jira: " + robot_brain)
robot.say(robot_brain)
robot.runAndWait()