import re

from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, lookup_hex_to_rgb


@bot.message_handler(commands=['about'])
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)


def _is_zodiac_command(message):
    regexp = r'/zodiac \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_shio_command(message):
    regexp = r'/shio \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_hextorgb_command(message):
    regexp = r'/colour #......'
    return re.match(regexp, message.text) is not None
    # A bit confused here, to match #ffffff how should the syntax be written?
    # E.x: To match the year for zodiac you use decimal but for '#' and abc symbols?


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


@bot.message_handler(func=_is_hextorgb_command)
def hex2rgb(message):
    app.logger.debug("'colour' command detected")
    _, colour_value = message.text.split(' ')
    app.logger.debug('colour = {}'.format(value))
    bot.reply_to(message, lookup_hex_to_rgb(value))


def _parse_date(text):
    return tuple(map(int, text.split('-')))
