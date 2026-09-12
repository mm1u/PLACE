import pyttsx3

guide = pyttsx3.init()

guide.setProperty("rate", 150)
guide.setProperty("volume", 1.0)

def speak(text):
    guide.say(text)
    guide.runAndWait()