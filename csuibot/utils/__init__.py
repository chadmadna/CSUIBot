from csuibot.utils import zodiac as z
from csuibot.utils import boardgame as b
from csuibot.utils import word as w


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


def draw_board(game):
    boards = [
        b.ChessBoard(),
        b.CheckersBoard(),
        b.ReversiBoard()
    ]

    for board in boards:
        if board.name == game:
            return str(board)
    return 'Not yet implemented, please send request to Irsyad Nabil.'


def draw_empty_board():
    return str(b.AbstractBoard())


def lookup_word(action, word):
    searches = [
        w.Definition(word),
        w.Synonym(word),
        w.Antonym(word)
    ]

    for search in searches:
        if search.name == action:
            return search.find


def lookup_hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    result = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return str(result)
