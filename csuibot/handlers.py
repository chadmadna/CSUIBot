import re

from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, lookup_answer


@bot.message_handler(commands=['about'])
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)

@bot.message_handler(commands=['yelfasilkom'])
def yelFasilkom(message):
    app.logger.debug("'yelfasilkom' command detected")
    yelfslkm_text = (
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
        "Fasilkom*\n"
        "* : Diikuti dengan gerakan menghentakkan kaki\n"
    )
    bot.reply_to(message, yelfslkm_text)


def _is_zodiac_command(message):
    regexp = r'/zodiac \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_shio_command(message):
    regexp = r'/shio \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None

def _is_answerbot_command(message):
    regexp = r'/speaknicely'
    return re.match(regexp, message.text) is not None


@bot.message_handler(func=_is_zodiac_command)
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = _parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))
    bot.reply_to(message, lookup_zodiac(month, day))


@bot.message_handler(func=_is_shio_command)
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = _parse_date(date_str)
    app.logger.debug('year = {}'.format(year))
    bot.reply_to(message, lookup_chinese_zodiac(year))

@bot.message_handler(func=_is_answerbot_command)
def answerBot(message):
    app.logger.debug("'answerbot' command detected")
    #app.logger.debug("answer = {}".format(res))
    bot.reply_to(message, lookup_answer(self))
    # do i need text split for a command without anything else after it. ex: /speaknicely [no additional message]; unlike /zodiac yyyy-mm-dd    
    


def _parse_date(text):
    return tuple(map(int, text.split('-')))
