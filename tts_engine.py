import pyttsx3
engine = pyttsx3.init(driverName='espeak')

def text_to_voice(text):
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()
    

