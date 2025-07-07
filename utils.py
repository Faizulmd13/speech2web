def get_first_words(text):

    command = text.strip().split()

    return command[0:3]

def clean_input(text):

    tokens = text.strip().split()
    if not tokens:
        return ["never", "gonna", "give", "you", "up"]
    elif tokens[0] == "play":
        return tokens[1:]
    elif tokens[:2] == ["put", "on"]:
        return tokens[2:]
    elif tokens[:3] == ["tell", "me", "about"]:
        return tokens[3:]
    else:
        return ["never", "gonna", "give", "you", "up"]