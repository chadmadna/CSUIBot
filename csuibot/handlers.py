import re

from . import app, bot
from .utils import (lookup_zodiac, lookup_chinese_zodiac, draw_board,
                    draw_empty_board, lookup_word, lookup_hex_to_rgb,
                    generate_chant)


def _is_zodiac_command(message):
    regexp = r'/zodiac \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_shio_command(message):
    regexp = r'/shio \d{4}\-\d{2}\-\d{2}'
    return re.match(regexp, message.text) is not None


def _is_compute_command(message):
    regexp = r'/compute ...'
    return re.match(regexp, message.text) is not None


def _is_board_command(message):
    regexp = r'/board( [a-z]+)?'
    return re.match(regexp, message.text) is not None


def _is_definition_command(message):
    regexp = r'/definition \S+$'
    return re.match(regexp, message.text) is not None


def _is_synonym_command(message):
    regexp = r'/synonym \S+$'
    return re.match(regexp, message.text) is not None


def _is_antonym_command(message):
    regexp = r'/antonym \S+$'
    return re.match(regexp, message.text) is not None


def _is_hextorgb_command(message):
    regexp = r'/colour #......'
    return re.match(regexp, message.text) is not None


@bot.message_handler(commands=['about'])
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)


@bot.message_handler(commands=['yelfasilkom'])
def yelfasilkom(message):
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
        "Fasilkom*\n\n"
        "* : Diikuti dengan gerakan menghentakkan kaki\n"
    )
    bot.reply_to(message, yelfslkm_text)


@bot.message_handler(func=_is_compute_command)
def compute(message):
    app.logger.debug("'compute' command detected")
    exp = message.text
    exp = exp[8:]
    error = 'you think you can add banana+apple? not happening man.'
    if re.search('[a-zA-Z]', exp):
        bot.reply_to(message, error)
    else:
        bot.reply_to(message, eval(exp))


def _is_chant_command(message):
    regexp = r'(?i)^(.*?(\bfasilkom\b)[^$]*)$'
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


@bot.message_handler(func=_is_hextorgb_command)
def hex2rgb(message):
    app.logger.debug("'colour' command detected")
    _, colour_value = message.text.split(' ')
    app.logger.debug('colour = {}'.format(colour_value))
    bot.reply_to(message, lookup_hex_to_rgb(colour_value))


@bot.message_handler(func=_is_definition_command)
def definition(message):
    app.logger.debug("'definition' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))


@bot.message_handler(func=_is_synonym_command)
def synonym(message):
    app.logger.debug("'synonym' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))


@bot.message_handler(func=_is_antonym_command)
def antonym(message):
    app.logger.debug("'antonym' command detected")
    action_str, word_str = _parse_word(message.text)
    app.logger.debug('action = {}, word = {}'.format(action_str, word_str))
    bot.reply_to(message, lookup_word(action_str, word_str))


def _parse_word(text):
    """Return first word if input contains multiple words."""
    ret = text[1:].split(' ')
    return ret[:2] if len(ret) > 2 else ret


def _parse_date(text):
    return tuple(map(int, text.split('-')))


@bot.message_handler(func=_is_chant_command)
def chant(message):
    app.logger.debug("'chant' command detected")
    bot.reply_to(message, generate_chant())
