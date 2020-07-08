from datetime import date, datetime
from say import say


def handle(you_said):
    while True:
        if you_said == "":
            robot_brain = "Sorry! I can't hear you, try again!"
        elif "hello" or "hi" in you_said:
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
        elif "bye" or "goodbye" in you_said:
            robot_brain = "Bye! Have a good day!"
            say(robot_brain)
            break
        else:
            robot_brain = "I'm fine, thank you and you."

        print("Jira: " + robot_brain)
        return robot_brain