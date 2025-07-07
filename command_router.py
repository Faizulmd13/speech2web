import utils

def router(text):
    command = utils.get_first_words(text)
    command = [word.lower() for word in command]

    if command[0] == "play" or command[:2] == ["put", "on"]:
        return 1
    elif command[:3] == ["tell", "me", "about"]:
        return 2
    else:
        return -1

