from csuibot.utils import zodiac as z
import random


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Leo(),
        z.Sagittarius(),
        z.Aquarius(),
        z.Gemini(),
        z.Cancer(),
        z.Scorpio()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = {
        0: 'rat',
        4: 'dragon',
        5: 'snake'
        }
    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except KeyError:
        return 'Unknown zodiac'

def lookup_answer(self):
    # Create an array containing the comments. hardcoded
    self.comments = ["Your kindness is a balm to all who encounter it.",
                "Jokes are funnier when you tell them.",
                "There's ordinary, and then there's you."
                ]
    # Function to parse the list and select randomly
    # then send to handlers.py. then handlers.py will reply to user.
    self.res = self.comments[random.randint(0, len(self.comments)-1)]
    return self.res

