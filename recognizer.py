import speech_recognition as sr
import sys

def audio_recognizer():
    r = sr.Recognizer()

    with sr.Microphone() as Source:
        print("Listening...")
        audio = r.listen(Source)

    try:
        command = r.recognize_google(audio, language="en-IN")
    except sr.UnknownValueError:
        print("Could not understand audio.")
        sys.exit()
    except sr.RequestError as e:
        print("Could not request results; check your internet connection.")
        sys.exit()

    return command

# text = audio_recognizer()
# print(text)