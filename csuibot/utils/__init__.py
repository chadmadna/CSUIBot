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

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

