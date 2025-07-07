import utils

def router(text):
    command = utils.get_first_words(text)
    command = command.lower()

    if command == "play":
        print("Opening Youtube")
    elif command == "put":
        print("Opening Youtube music")
    elif command == "tell":
        print("Opening Wikipedia")
    else:
        print("Not a supported commands")

