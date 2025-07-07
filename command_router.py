import utils

def router(text):
    command = utils.get_first_words(text)
    command = [word.lower() for word in command]

    if command[0] == "play" or command[:2] == ["put", "on"]:
        return 1
    else:
        return -1

