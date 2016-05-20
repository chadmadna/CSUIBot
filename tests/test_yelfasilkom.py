from unittest.mock import Mock

#from csuibot.handlers import help, zodiac, shio


def test_yelfasilkom(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()
    yelFasilkom(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        "Aba-aba pembuka: Fasilkom!!!\n"
        "Fasilkom!*"
        "Ilmu Komputer"
        "Fasilkom!*"
        "Satu Banding Seratus"
        "Kami Elit, Kami Kompak, Kami Anak UI"
        "MIPA Bukan, Teknik Bukan,"
        "FE Apalagi*"
        "Kami ini Fakultas No.1 di UI"
        "Kami Cinta Fasilkom"
        "Kami Bangga Fasilkom"
        "Maju Terus"
        "Fasilkom*\n"
        "* : Diikuti dengan gerakan menghentakkan kaki"
    )
    assert args[1] == expected_text
