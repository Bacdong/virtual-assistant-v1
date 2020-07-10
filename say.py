import pyttsx3

# robot_brain = "Hello, I am Jira. I'm the Virtual Assistant of Bacdong!"

def say(robot_brain):

    robot = pyttsx3.init()
    voices = robot.getProperty('voices') 
    robot.setProperty('voice', voices[1].id) 

    rate = robot.getProperty('rate')  
    robot.setProperty('rate', 135)

    robot.say(robot_brain)
    robot.runAndWait()

say(robot_brain)