import random

class TestAnswer:
    def __init__(self):
        self.comments = ["Your kindness is a balm to all who encounter it.",
                "Jokes are funnier when you tell them.",
                "There's ordinary, and then there's you."
                ]
    def match(self):
        # Checks whether the randomly selected comments matches one of the predefined answers (in a list).
        res = self.comments[random.randint(0, len(self.comments)-1)]
        for char in self.comments:
            print (res)
            print (char)
            if char == res:
                return (True)
                #print ("Matches to array")
            else:
                raise LookupError
    
def main():
    testans = TestAnswer()
    testans.match()

main()

#from csuibot import utils

#class TestAnswer:

#   def test_match(self):
#       how to assert if theres many variations???
