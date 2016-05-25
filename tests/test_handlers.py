from unittest.mock import Mock

from csuibot.handlers import help, zodiac, shio, yelfasilkom, compute, board, definition, synonym, antonym


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
