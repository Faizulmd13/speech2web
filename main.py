from recognizer import audio_recognizer
from command_router import router
import web_actions

def main():
    text = audio_recognizer()
    
    code = router(text)

    if code == 1:
        web_actions.youtube(text)
    elif code == 2:
        pass
    else:
        web_actions.youtube(text)

main()