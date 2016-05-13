

class TestAnswer:
    comments = ["Your kindness is a balm to all who encounter it.",
            "Jokes are funnier when you tell them.",
            "There's ordinary, and then there's you."
            ]
    def match(self):
        # Checks whether the randomly selected comments matches one of the predefined answers (in a list).
        res = comments[random.randint(0, len(comments))]
        for char in range (len(comments)):
            if char == res:
                print ("Matches to array")
            else:
                print ("Got nothing")
    
