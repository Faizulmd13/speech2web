def get_first_words(text):
    command = text.strip().split()
    return command[0:3]

def clean_input(text):

    tokens = text.strip().split()

    if tokens[0] == "play":
        return tokens[1:]
    elif tokens[:2] == ["put", "on"]:
        return tokens[2:]
    else:
        return []
    
