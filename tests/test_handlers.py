from unittest.mock import Mock

<<<<<<< HEAD
from csuibot.handlers import help, zodiac, shio, compute
=======
from csuibot.handlers import help, zodiac, shio, board
>>>>>>> 14bc0dacc7443f4df367e60204cd0323159bdfd4


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


<<<<<<< HEAD
def test_compute1(mocker):
    fake_compute1 = 'Error'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/compute aa+bb')
    res = compute(mock_message)
    if res != 'ERROR: This is not a math expression.':
        raise AssertionError("Wrong Result")


##def test_compute2(mocker):
##    fake_compute2 = '
##    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
##    mock_message = Mock(text='/compute "hallo world"')
##    res = compute(mock_message)
##    if res != 'ERROR: This is not a math expression.':
##        raise AssertionError("Wrong Result")


def test_compute3(mocker):
    fake_compute3 = '12'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/compute 5+7')
    res = compute(mock_message)
    if res != 'ERROR: This is not a math expression.':
        raise AssertionError("wrong Result")
=======
def test_board(mocker):
    fake_board = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.draw_board', return_value=fake_board)
    mock_message = Mock(text='/board checkers')
    board(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_board
>>>>>>> 14bc0dacc7443f4df367e60204cd0323159bdfd4
