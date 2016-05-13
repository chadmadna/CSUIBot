import re

from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, draw_board, draw_empty_board


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


def _is_board_command(message):
    regexp = r'/board( [a-z]+)?'
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


@bot.message_handler(func=_is_board_command)
def board(message):
    app.logger.debug("'board' command detected")
    msg_str = message.text.split(' ')
    if len(msg_str) == 1:
        app.logger.debug('empty board')
        bot.reply_to(message, draw_empty_board())
    else:
        _, game = msg_str
        app.logger.debug('game = {}'.format(game))
        bot.reply_to(message, draw_board(game))


def _parse_date(text):
    return tuple(map(int, text.split('-')))
