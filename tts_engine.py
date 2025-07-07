import pyttsx3
engine = pyttsx3.init()

def text_to_voice(text):
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()
    

