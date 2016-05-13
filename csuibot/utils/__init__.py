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
        z.Scorpio(),
        z.Libra()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name
    else:
        return 'Unknown zodiac'


def lookup_chinese_zodiac(year):
    num_zodiacs = 12

    zodiacs = {
        0: 'rat',
        1: 'buffalo',
        2: 'tiger',
        4: 'dragon',
        5: 'snake',
        6: 'horse',
        7: 'goat',
        8: 'monkey'
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
