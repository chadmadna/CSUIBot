from unittest.mock import MagicMock
from csuibot import utils
from csuibot.utils import word
from csuibot.utils import kbbi
from csuibot.utils import sound
import json


class TestLyricSearch:

    def test_lyric_search(self, mocker):
        class FakeResponse:
            def json(self):
                track_list = [
                    {
                        'track': {
                            'track_name': 'woof',
                            'artist_name': 'dog'
                        }
                    },
                    {
                        'track': {
                            'track_name': 'meow',
                            'artist_name': 'cat'
                        }
                    }
                ]
                return {
                    'message': {
                        'body': {
                            'track_list': track_list
                        }
                    }
                }

        expected_text = (
            'Possible Songs:\n'
            'woof by dog\n'
            'meow by cat\n'
            )

        mocked_get = mocker.patch('requests.get', return_value=FakeResponse())
        res = utils.lyric_search('blabla')
        _, kwargs = mocked_get.call_args

        assert 'params' in kwargs
        assert 'q_lyrics' in kwargs['params']
        assert kwargs['params']['q_lyrics'] == 'blabla'
        assert res == expected_text


class TestZodiac:

    def test_taurus_lower_bound(self):
        res = utils.lookup_zodiac(4, 20)
        assert res == 'taurus'

    def test_taurus_upper_bound(self):
        res = utils.lookup_zodiac(5, 20)
        assert res == 'taurus'

    def test_taurus_in_between(self):
        res = utils.lookup_zodiac(4, 30)
        assert res == 'taurus'

    def test_not_taurus(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'taurus'

    def test_aries_lower_bound(self):
        res = utils.lookup_zodiac(3, 21)
        assert res == 'aries'

    def test_aries_upper_bound(self):
        res = utils.lookup_zodiac(4, 19)
        assert res == 'aries'

    def test_aries_in_between(self):
        res = utils.lookup_zodiac(4, 1)
        assert res == 'aries'

    def test_not_aries(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'aries'

    def test_leo_lower_bound(self):
        res = utils.lookup_zodiac(7, 23)
        assert res == 'leo'

    def test_leo_upper_bound(self):
        res = utils.lookup_zodiac(8, 22)
        assert res == 'leo'

    def test_leo_in_between(self):
        res = utils.lookup_zodiac(8, 8)
        assert res == 'leo'

    def test_not_leo(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'leo'

    def test_sagittarius_lower_bound(self):
        res = utils.lookup_zodiac(11, 22)
        assert res == 'sagittarius'

    def test_sagittarius_upper_bound(self):
        res = utils.lookup_zodiac(12, 21)
        assert res == 'sagittarius'

    def test_sagittarius_in_between(self):
        res = utils.lookup_zodiac(12, 12)
        assert res == 'sagittarius'

    def test_not_sagittarius(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'sagittarius'

    def test_aquarius_lower_bound(self):
        res = utils.lookup_zodiac(1, 20)
        assert res == 'aquarius'

    def test_aquarius_upper_bound(self):
        res = utils.lookup_zodiac(2, 18)
        assert res == 'aquarius'

    def test_aquarius_in_between(self):
        res = utils.lookup_zodiac(2, 2)
        assert res == 'aquarius'

    def test_not_aquarius(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'aquarius'

    def test_gemini_lower_bound(self):
        res = utils.lookup_zodiac(5, 21)
        assert res == 'gemini'

    def test_gemini_upper_bound(self):
        res = utils.lookup_zodiac(6, 20)
        assert res == 'gemini'

    def test_gemini_in_between(self):
        res = utils.lookup_zodiac(6, 6)
        assert res == 'gemini'

    def test_not_gemini(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'gemini'

    def test_cancer_lower_bound(self):
        res = utils.lookup_zodiac(6, 21)
        assert res == 'cancer'

    def test_cancer_upper_bound(self):
        res = utils.lookup_zodiac(7, 19)
        assert res == 'cancer'

    def test_cancer_in_between(self):
        res = utils.lookup_zodiac(7, 1)
        assert res == 'cancer'

    def test_not_cancer(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'cancer'

    def test_scorpio_lower_bound(self):
        res = utils.lookup_zodiac(10, 23)
        assert res == 'scorpio'

    def test_scorpio_upper_bound(self):
        res = utils.lookup_zodiac(11, 21)
        assert res == 'scorpio'

    def test_scorpio_in_between(self):
        res = utils.lookup_zodiac(11, 11)
        assert res == 'scorpio'

    def test_not_scorpio(self):
        res = utils.lookup_zodiac(11, 27)
        assert res != 'scorpio'

    def test_libra_lower_bound(self):
        res = utils.lookup_zodiac(9, 23)
        assert res == 'libra'

    def test_libra_upper_bound(self):
        res = utils.lookup_zodiac(10, 22)
        assert res == 'libra'

    def test_libra_in_between(self):
        res = utils.lookup_zodiac(10, 10)
        assert res == 'libra'

    def test_not_libra(self):
        res = utils.lookup_zodiac(11, 17)
        assert res != 'libra'


class TestChineseZodiac:
    def run_test(self, expected_zodiac, years):
        res = [utils.lookup_chinese_zodiac(y) == expected_zodiac for y in years]

        assert all(res)

    def test_buffalo(self):
        years = [1997, 1985, 1973, 1961, 2009, 2021]
        self.run_test('buffalo', years)

    def test_rat(self):
        years = [1996, 1984, 1972, 1960, 2008, 2020]
        self.run_test('rat', years)

    def test_dragon(self):
        years = [2000, 1988, 1976, 1964, 2012, 2024]
        self.run_test('dragon', years)

    def test_snake(self):
        years = [2001, 1989, 1977, 1965, 2013, 2025]
        self.run_test('snake', years)

    def test_goat(self):
        years = [2003, 1991, 1979, 1967, 2015, 2027]
        self.run_test('goat', years)

    def test_monkey(self):
        years = [2004, 1992, 1980, 1968, 2016, 2028]
        self.run_test('monkey', years)

    def test_horse(self):
        years = [2002, 1990, 1978, 1966, 2014, 2026]
        self.run_test('horse', years)

    def test_tiger(self):
        years = [1998, 1986, 1974, 1962, 2010, 2022]
        self.run_test('tiger', years)

    def test_unknown_zodiac(self):
        years = [2005, 1993, 1981, 1969, 2017, 2029]
        self.run_test('Unknown zodiac', years)


class TestBoardGame:
    def test_empty_board(self):
        res = ("\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\n"
               "\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\n") * 4

        assert utils.draw_empty_board() == res

    def test_chess_board(self):
        black = "\U0001f3e4\U0001f40e\U0001f473\U0001f470" \
                "\U0001f468\U0001f473\U0001f40e\U0001f3e4\n" \
                "\U0001f466\U0001f466\U0001f466\U0001f466" \
                "\U0001f466\U0001f466\U0001f466\U0001f466\n"

        empty = ("\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\n"
                 "\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\n") * 2

        white = "\U0001f467\U0001f467\U0001f467\U0001f467" \
                "\U0001f467\U0001f467\U0001f467\U0001f467\n" \
                "\u26ea\U0001f417\U0001f472\U0001f478" \
                "\U0001f474\U0001f472\U0001f417\u26ea\n"

        assert utils.draw_board("chess") == black + empty + white

    def test_checkers_board(self):
        black = ("\u2b1c\u26ab\u2b1c\u26ab\u2b1c\u26ab\u2b1c\u26ab\u2b1c\u26ab\n"
                 "\u26ab\u2b1c\u26ab\u2b1c\u26ab\u2b1c\u26ab\u2b1c\u26ab\u2b1c\n") * 2

        empty = "\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\n" \
                "\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\u2b1b\u2b1c\n"

        white = ("\u2b1c\u26aa\u2b1c\u26aa\u2b1c\u26aa\u2b1c\u26aa\u2b1c\u26aa\n"
                 "\u26aa\u2b1c\u26aa\u2b1c\u26aa\u2b1c\u26aa\u2b1c\u26aa\u2b1c\n") * 2

        assert utils.draw_board("checkers") == black + empty + white

    def test_reversi_board(self):
        empty = "\u2b1c\u2b1c\u2b1c\u2b1c\u2b1c\u2b1c\u2b1c\u2b1c\n" * 3

        center = "\u2b1c\u2b1c\u2b1c\u26aa\u26ab\u2b1c\u2b1c\u2b1c\n" \
                 "\u2b1c\u2b1c\u2b1c\u26ab\u26aa\u2b1c\u2b1c\u2b1c\n"

        assert utils.draw_board("reversi") == empty + center + empty


class TestWord:
    def create_fake_init(self, name, mean=None):
        def fake_init(slf, word):
            slf.name = name
            slf.mean = mean
            slf.find = slf.lookup()

        return fake_init

    def test_definition(self, mocker):
        mocker.patch.object(word.Definition, '__init__',
                            self.create_fake_init('definition', {'foo': ['bar']}))
        mocker.patch.object(word.Synonym, '__init__', self.create_fake_init('synonym'))
        mocker.patch.object(word.Antonym, '__init__', self.create_fake_init('antonym'))

        assert utils.lookup_word('definition', 'test') == 'foo\n1. bar\n\n'

    def test_definition_not_found(self, mocker):
        mocker.patch.object(word.Definition, '__init__', self.create_fake_init('definition'))
        mocker.patch.object(word.Synonym, '__init__', self.create_fake_init('synonym'))
        mocker.patch.object(word.Antonym, '__init__', self.create_fake_init('antonym'))

        assert utils.lookup_word('definition', 'test') == 'Invalid word'

    def test_synonym(self, mocker):
        mocker.patch.object(word.Definition, '__init__', self.create_fake_init('definition'))
        mocker.patch.object(word.Synonym, '__init__',
                            self.create_fake_init('synonym', ['foo', 'bar']))
        mocker.patch.object(word.Antonym, '__init__', self.create_fake_init('antonym'))

        assert utils.lookup_word('synonym', 'test') == 'foo bar '

    def test_synonym_not_found(self, mocker):
        mocker.patch.object(word.Definition, '__init__', self.create_fake_init('definition'))
        mocker.patch.object(word.Synonym, '__init__', self.create_fake_init('synonym'))
        mocker.patch.object(word.Antonym, '__init__', self.create_fake_init('antonym'))

        assert utils.lookup_word('synonym', 'test') == 'Invalid word'

    def test_antonym(self, mocker):
        mocker.patch.object(word.Definition, '__init__', self.create_fake_init('definition'))
        mocker.patch.object(word.Synonym, '__init__', self.create_fake_init('synonym'))
        mocker.patch.object(word.Antonym, '__init__',
                            self.create_fake_init('antonym', ['foo', 'bar']))

        assert utils.lookup_word('antonym', 'test') == 'foo bar '

    def test_antonym_not_found(self, mocker):
        mocker.patch.object(word.Definition, '__init__', self.create_fake_init('definition'))
        mocker.patch.object(word.Synonym, '__init__', self.create_fake_init('synonym'))
        mocker.patch.object(word.Antonym, '__init__', self.create_fake_init('antonym'))

        assert utils.lookup_word('antonym', 'test') == 'Invalid word'


class TestChant:

    def test_chant(self):
        res = "Viva, Viva, Viva Fasilkom!"
        assert utils.generate_chant() == res


class TestPlants:

    def test_plants_trivia(self):
        res = utils.lookup_plants_trivia(['Dandellions are yellow'])
        assert res == 'Dandellions are yellow'

    def test_plants_trivia_file(self):
        res = utils.lookup_plants_trivia()
        compare = open(
            'assets/plants_trivia.txt',
            'r', encoding='utf-8-sig').readlines()
        compare = [lines.strip() for lines in compare]
        assert res in compare


class TestDefinisi:

    def test_url_data(self, mocker):
        fake_json = dict(foo='bar')

        class FakeResponse:

            def json(self):
                return fake_json

        mocker.patch("csuibot.utils.kbbi.requests.get", return_value=FakeResponse())
        assert kbbi.WordDefinition('test').url_data() == fake_json

    def test_definition(self, mocker):
        fake_data = {'kateglo': {'definition': [{'def_text': 'foo'}]}}
        fake_text = "(1)foo"
        mocker.patch("csuibot.utils.kbbi.WordDefinition.url_data", return_value=fake_data)
        assert kbbi.WordDefinition('test').definition() == fake_text

    def test_definisi_output(self, mocker):
        fake_data = {'kateglo': {'definition': [{'def_text': 'foo'}]}}
        fake_text = "test" + "\n" + "(1)foo"
        mocker.patch("csuibot.utils.kbbi.WordDefinition.url_data", return_value=fake_data)
        assert utils.lookup_definisi('test') == fake_text

    def test_wrong_word(self, mocker):
        class FakeResponse:
            def json(self):
                raise json.decoder.JSONDecodeError('msg', 'doc', 123)

        expected = 'Oooopss, It looks like you type the wrong word!'
        mocker.patch("csuibot.utils.kbbi.requests.get", return_value=FakeResponse())
        assert kbbi.WordDefinition('test').url_data() == expected
        assert utils.lookup_definisi('test') == 'test' + '\n' + expected


class TestVisualFeatures:
    @staticmethod
    def create_fake_features():
        def fake_features(slf):
            slf._categories = "Foo > Bar"
            slf._tags = "foo, bar, baz"
            slf._description = "A foo borking a bar"
            slf._faces = [
                {'gender': 'foo', 'age': 20},
                {'gender': 'bar', 'age': 25},
            ]
            slf._image_type = 'Clipart'
            slf._color = {'dominant': ['Foo'], 'fg': 'Bar',
                          'bg': 'Baz', 'accent': '666666',
                          'is_bw': False}
            slf._is_adult = (False, False)

        return fake_features

    @staticmethod
    def create_fake_init_feature(data, attr):
        def fake_feature(slf, imginfo):
            slf._data = data
            setattr(slf, attr, getattr(slf, '_fetch{}'.format(attr))())

        return fake_feature

    def test_get_visual_features(self, mocker):
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch('csuibot.utils.visualfeatures.requests')
        mocker.patch('csuibot.utils.visualfeatures.json.loads')
        mocker.patch.object(utils.v.ImgRequest, 'init_features', self.create_fake_features())
        response = 'A foo borking a bar.\n\nCategories: Foo > Bar\nTags: foo, bar, baz' \
                   '\nFaces: 2 face(s) identified:\n- foo, 20 years old\n- bar, 25 ' \
                   'years old\nImage type: Clipart\nColor profile: \n- Dominant color: ' \
                   'Foo\n  * Foreground color: Bar\n  * Background color: Baz\n- ' \
                   'Accent color: #666666\n- Is a B/W image: False\nIs adult content: ' \
                   'False\nIs racy content: False'

        assert utils.get_visual_features(fake_file) == response

    def test_fetch_categories(self, mocker):
        fake_data = {'categories': [
            {'score': 0.3515625, 'name': 'people_'},
            {'score': 0.64453125, 'name': 'people_show'}
        ]}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_categories'))
        response = 'People > Show'

        assert utils.v.ImgRequest(fake_file).categories == response

    def test_fetch_tags(self, mocker):
        fake_data = {'tags': [
            {'confidence': 0.9515625, 'name': 'show'},
            {'confidence': 0.9445312, 'name': 'concert'},
            {'confidence': 0.9198734, 'name': 'television'},
            {'confidence': 0.8902537, 'name': 'woman'},
            {'confidence': 0.8502343, 'name': 'music'},
            {'confidence': 0.8392349, 'name': 'guitar'}
        ]}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_tags'))
        response = 'show, concert, television, woman, music'

        assert utils.v.ImgRequest(fake_file).tags == response

    def test_fetch_description(self, mocker):
        fake_data = {
            'description': {
                'captions': [
                    {'confidence': 0.714, 'text': 'a foo borking a bar'},
                    {'confidence': 0.946, 'text': 'a foobar borking into '
                                                  'MAXIMUM BORKDRIVE'},
                    ]
                }
        }
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_description'))
        response = 'A foobar borking into MAXIMUM BORKDRIVE'

        assert utils.v.ImgRequest(fake_file).description == response

    def test_fetch_faces(self, mocker):
        fake_data = {'faces': [
            {'gender': 'Betina', 'age': 60},
            {'gender': 'Pejantan', 'age': 35}
        ]}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_faces'))
        response = [{'gender': 'Betina', 'age': 60},
                    {'gender': 'Pejantan', 'age': 35}]

        assert utils.v.ImgRequest(fake_file).faces == response

    def test_fetch_image_type(self, mocker):
        fake_data = {'imageType': {'lineDrawingType': 0, 'clipArtType': 2}}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_image_type'))
        response = 'Clipart'

        assert utils.v.ImgRequest(fake_file).image_type == response

    def test_fetch_color(self, mocker):
        fake_data = {'color': {
            'accentColor': '671188',
            'dominantColorBackground': 'Black',
            'dominantColorForeground': 'Red',
            'dominantColors': ['Black', 'Purple'],
            'isBWImg': False
        }}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_color'))
        response = {'bg': 'Black', 'fg': 'Red', 'dominant': ['Black', 'Purple'],
                    'accent': '671188', 'is_bw': False}

        assert utils.v.ImgRequest(fake_file).color == response

    def test_fetch_is_adult(self, mocker):
        fake_data = {'adult': {
            'racyScore': 0.04737820103764534,
            'isRacyContent': False,
            'adultScore': 0.04082706198096275,
            'isAdultContent': False
        }}
        fake_file = mocker.Mock(spec=['file_path'])
        mocker.patch.object(utils.v.ImgRequest, '__init__',
                            self.create_fake_init_feature(fake_data, '_is_adult'))
        response = (False, False)

        assert utils.v.ImgRequest(fake_file).is_adult == response


class TestSound:

    """
    1. Mock self.client value to None, or omit the variable altogether
    2. Run self.get_tracks() for self.trx where the return values are:
       - A list containing an instance of the object FakeTracks
       - An empty list to raise HTTPError
    3. Unit tests to parse the tracks and duration are otherwise OK
    """

    class FakeTracks:
        def __init__(self, title, duration, user, permalink_url):
            self.title = title
            self.duration = duration
            self.user = user
            self.permalink_url = permalink_url

    def create_fake_init(self, action, keyword):
        def fake_init(slf, action, keyword):
            slf.action = action
            slf.keyword = keyword
            slf.trx = [TestSound.FakeTracks('Foo Bar', 1000, {'username': 'The Foo Bar Band'},
                                            'http://www.google.com')]
            slf.lookup = slf._parse_tracks()
        return fake_init

    def test_sound_composer(self, mocker):
        mocker.patch.object(sound.Sound, '__init__',
                            self.create_fake_init('sound_composer', 'foo bar'))
        res = """TRACK NAME Foo Bar
DURATION 00:01
COMPOSER The Foo Bar Band
URL http://www.google.com

"""

        assert utils.lookup_sound('sound_composer', 'foo bar') == res

    def test_sound_search(self, mocker):
        mocker.patch.object(sound.Sound, '__init__',
                            self.create_fake_init('sound_search', 'foo bar'))
        res = """TRACK NAME Foo Bar
DURATION 00:01
COMPOSER The Foo Bar Band
URL http://www.google.com

"""

        assert utils.lookup_sound('sound_search', 'foo bar') == res


class TestCognitiveNews:
    def test_search(self):
        fake_dict = {"fake_key": "fake_value"}
        res = MagicMock(utils.search_news("Lorem Ipsum"), return_value=fake_dict)
        res("Lorem Ipsum")
        res.assert_called_with("Lorem Ipsum")
