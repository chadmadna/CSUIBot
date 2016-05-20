from unittest.mock import Mock

from csuibot.handlers import help, zodiac, shio, yelFasilkom


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

def test_yelFasilkom(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()
    yelFasilkom(mock_message)

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
