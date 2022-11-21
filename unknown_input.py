import random


def unknown():  # if steve doesn't find any matches within the user input
    response = ["I don't understand? ",  # Steve will provide one of the following statements
                "Huh?",
                "Que?",
                "Wait, what?",
                "I don't know what that means, but sure!",
                "I'm sorry, I can't understand what you're saying."][
        random.randrange(6)]
    return response
