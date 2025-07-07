from recognizer import audio_recognizer
from command_router import router

def main():
    text = audio_recognizer()
    
    router(text)

main()