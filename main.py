from recognizer import audio_recognizer
from command_router import router
import web_access 
import time

def main():
    while(True):
        text = audio_recognizer()
        
        code = router(text)

        if code == 1:
            web_access.youtube(text)
            break
        else:
            time.sleep(5)


main()