import speech_recognition

def hear():
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Jira: I'm Listening...")
        audio = robot_ear.listen(mic)
    print("Jira: ...")
    try:
        you_said = robot_ear.recognize_google(audio)
    except:
        you_said = "Jira: Sorry! I dit not hear what you said, try again!"

    print("You: " + you_said)
    return you_said
