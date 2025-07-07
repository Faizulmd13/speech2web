import utils
from tts_engine import text_to_voice

def router(text):
    command = utils.get_first_words(text)
    command = [word.lower() for word in command]
    if not command:
        msg = "Please Speak again"
        print(msg)
        text_to_voice(msg)
        return -1
    elif command[0] == "play" or command[:2] == ["put", "on"]:
        return 1
    else:
        msg = "Say something like Play Kulosa or put on Kulosa"
        print(msg)
        text_to_voice(msg)
        return -2

