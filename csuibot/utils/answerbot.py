import random

class Answer:
    def __init__(self):
        # Create an array containing the comments. hardcoded
        self.comments = ["Your kindness is a balm to all who encounter it.",
                    "Jokes are funnier when you tell them.",
                    "There's ordinary, and then there's you."
                    ]
        # Function to parse the list and select randomly
        # then send to handlers.py. then handlers.py will reply to user.
        self.res = self.comments[random.randint(0, len(self.comments)-1)]
