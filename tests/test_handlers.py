from unittest.mock import Mock
from csuibot.handlers import (help, zodiac, shio, yelfasilkom, compute,
                              board, definition, synonym, antonym, hex2rgb,
                              date, time, chant, top_posters, get_messages,
                              message_dic, total_messages, lyricsearch,
                              plants)
from datetime import datetime


def test_help(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()
    help(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    assert args[1] == expected_text


def test_date(mocker):
    fake_date = datetime(2016, 5, 27)
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.get_current_date', return_value=fake_date)
    mock_message = '/date'
    date(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == 'Fri, 27 May 2016'


def test_time(mocker):
    fake_data = datetime(2016, 5, 27, 4, 10)
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.get_current_time', return_value=fake_data)
    mock_message = '/time'
    time(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == '11:10 AM (GMT+7)'


def test_top_posters(mocker):
    class Chat:
        def __init__(self, id, type):
            self.id = id
            self.type = type

    class Message:
        def __init__(self, chat):
            self.chat = chat

    fake_dic = {
        1: {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5
        }
    }

    fake_total = {
        1: 15
    }

    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch.dict(message_dic, fake_dic)
    mocker.patch.dict(total_messages, fake_total)
    message = Message(Chat(1, 'group'))
    top_posters(message)

    expected_text = (
        'Top 5 Posters:\n'
        '1. five (33.33%)\n'
        '2. four (26.67%)\n'
        '3. three (20.00%)\n'
        '4. two (13.33%)\n'
        '5. one (6.67%)\n'
        )

    args, _ = mocked_reply_to.call_args
    assert args[1] == expected_text


def test_get_messages(mocker):
    class Chat:
        def __init__(self, id, type):
            self.id = id
            self.type = type

    class User:
        def __init__(self, first_name):
            self.first_name = first_name

    class Message:
        def __init__(self, chat, user):
            self.chat = chat
            self.from_user = user

    expected_message_dic = {1: {'Cow': 2, 'Sheep': 1}, 2: {'Chicken': 1}}
    expected_total_messages = {1: 3, 2: 1}

    message0 = Message(Chat(1, 'group'), User('Cow'))
    message1 = Message(Chat(1, 'group'), User('Cow'))
    message2 = Message(Chat(1, 'group'), User('Sheep'))
    message3 = Message(Chat(2, 'group'), User('Chicken'))
    messages = [message0, message1, message2, message3]

    for message in messages:
        get_messages(message)

    assert message_dic == expected_message_dic
    assert total_messages == expected_total_messages


def test_lyricsearch(mocker):
    fake_songs = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lyric_search', return_value=fake_songs)
    mock_message = Mock(text='/lyricsearch love')
    lyricsearch(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_songs


def test_zodiac_argument(mocker):
    prompt_txt = 'Please input the date in yyyy-mm-dd format, e.g. 1998-05-02'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/zodiac')
    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == prompt_txt


def test_shio_argument(mocker):
    prompt_txt = 'Please input the date in yyyy-mm-dd format, e.g. 1998-05-02'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/shio')
    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == prompt_txt


def test_zodiac(mocker):
    fake_zodiac = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', return_value=fake_zodiac)
    mock_message = Mock(text='/zodiac 2015-05-05')
    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_zodiac


def test_shio(mocker):
    fake_shio = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', return_value=fake_shio)
    mock_message = Mock(text='/shio 2015-05-05')
    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_shio


def test_compute1(mocker):
    fake_compute1 = 'you think you can add banana+apple? not happening man.'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/compute aa+bb')
    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_compute1


def test_board(mocker):
    fake_board = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.draw_board', return_value=fake_board)
    mock_message = Mock(text='/board checkers')
    board(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_board


def test_definition(mocker):
    fake_definition = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_definition)
    mock_message = Mock(text='/definition test')
    definition(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_definition


def test_synonym(mocker):
    fake_synonym = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_synonym)
    mock_message = Mock(text='/synonym test')
    synonym(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_synonym


def test_antonym(mocker):
    fake_antonym = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_word', return_value=fake_antonym)
    mock_message = Mock(text='/antonym test')
    antonym(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_antonym


def test_yelfasilkom(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()
    yelfasilkom(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        "Aba-aba pembuka: Fasilkom!!!\n"
        "Fasilkom!*\n"
        "Ilmu Komputer\n"
        "Fasilkom!*\n"
        "Satu Banding Seratus\n"
        "Kami Elit, Kami Kompak, Kami Anak UI\n"
        "MIPA Bukan, Teknik Bukan,\n"
        "FE Apalagi*\n"
        "Kami ini Fakultas No.1 di UI\n"
        "Kami Cinta Fasilkom\n"
        "Kami Bangga Fasilkom\n"
        "Maju Terus\n"
        "Fasilkom*\n\n"
        "* : Diikuti dengan gerakan menghentakkan kaki\n"
    )
    assert args[1] == expected_text


def test_hextorgb(mocker):
    fake_rgb = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_hex_to_rgb', return_value=fake_rgb)
    mock_message = Mock(text='/synonym test')
    hex2rgb(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_rgb


def test_chant(mocker):
    fake_chant = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.generate_chant', return_value=fake_chant)
    mock_message = Mock(text='Saya anak Fasilkom UI.')
    chant(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_chant


def test_plants(mocker):
    fake_trivia = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_plants_trivia', return_value=fake_trivia)
    mock_message = Mock(text='/plants')
    plants(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_trivia
