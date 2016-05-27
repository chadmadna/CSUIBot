from csuibot.utils import zodiac as z
from csuibot.utils import kbbi as k
from csuibot.utils import boardgame as b
from csuibot.utils import word as w
from csuibot.utils import plants as p
from csuibot.utils import visualfeatures as v
from csuibot.utils import sound as s
from csuibot import app
import requests


def lyric_search(lyrics):
    apikey = app.config['MUSIXMATCH_API']
    service_url = 'http://api.musixmatch.com/ws/1.1/track.search'
    sugg = 'Possible Songs:\n'
    r = requests.get(service_url, params=dict(q_lyrics=lyrics, apikey=apikey))
    json_resp = r.json()
    tracks = json_resp['message']['body']['track_list']
    for element in tracks[0:5]:
        track = element['track']['track_name']
        artist = element['track']['artist_name']
        app.logger.debug('{} by {}'.format(track, artist))
        sugg = sugg + '{} by {}\n'.format(track, artist)
    return sugg if tracks else 'No songs found!'


def lookup_zodiac(month, day):
    zodiacs = [
        z.Taurus(),
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


def lookup_sound(action, keyword):
    return s.Sound(action, keyword).lookup


def lookup_hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    result = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return str(result)


def generate_chant():
    return "Viva, Viva, Viva Fasilkom!"


def lookup_plants_trivia(plants_facts=None):
    result = p.Plants(plants_facts)
    return result.facts()


def lookup_definisi(text):
    definisi = k.WordDefinition(text).definition()
    return text + '\n' + definisi


def lookup_visual_features(imgfile):
    pass


def get_visual_features(imginfo):
    img = v.ImgRequest(imginfo)
    paragraph = "{}.\n\n" \
                "Categories: {}\n" \
                "Tags: {}\n" \
                "Faces: {}\n" \
                "Image type: {}\n" \
                "Color profile: {}\n" \
                "Is adult content: {}\n" \
                "Is racy content: {}"

    face_txt = "{}, {} years old"
    facelist = [face_txt.format(face['gender'], face['age']) for face in img.faces]
    newline = "\n- " if facelist else ""
    faces = "{} face(s) identified:{}{}".format(len(img.faces), newline,
                                                "\n- ".join(facelist))

    color = "\n- Dominant color: {}" \
            "\n  * Foreground color: {}" \
            "\n  * Background color: {}" \
            "\n- Accent color: #{}" \
            "\n- Is a B/W image: {}"\
        .format(", ".join(img.color['dominant']),
                img.color['fg'],
                img.color['bg'],
                img.color['accent'],
                img.color['is_bw']
                )

    paragraph = paragraph.format(img.description, img.categories,
                                 img.tags, faces, img.image_type,
                                 color, img.is_adult[0],
                                 img.is_adult[1])

    return paragraph
