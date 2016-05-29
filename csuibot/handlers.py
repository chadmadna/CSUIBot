import re
import operator
from time import gmtime, mktime
from datetime import datetime
from collections import defaultdict
from . import app, bot
from .utils import (lookup_zodiac, lookup_chinese_zodiac, draw_board,
                    draw_empty_board, lookup_word, lookup_hex_to_rgb,
                    generate_chant, lyric_search, lookup_plants_trivia,
                    lookup_definisi)

message_dic = defaultdict(dict)
total_messages = defaultdict(int)


def _is_zodiac_command(message):
    regexp = r'/zodiac( \d{4}\-\d{2}\-\d{2})?$'
    return re.match(regexp, message.text) is not None


def _is_shio_command(message):
    regexp = r'/shio( \d{4}\-\d{2}\-\d{2})?$'
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


def _lyric_search_command(message):
    regexp = r'/lyricsearch \w+'
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
    n = len('/compute ')
    exp = message.text[n:]
    error_msg = 'you think you can add banana+apple? not happening man.'
    if re.search('[^0-9\+\-\*/]', exp):
        bot.reply_to(message, error_msg)
    else:
        try:
            result = eval(exp)
        except:  # catch any exception
            bot.reply_to(message, error_msg)
        else:
            bot.reply_to(message, result)


def _is_chant_command(message):
    regexp = r'(?i)^(.*?(\bfasilkom\b)[^$]*)$'
    return re.match(regexp, message.text) is not None


def _is_definisi_command(message):
    regexp = r'/definisi \S+$'
    return re.match(regexp, message.text) is not None


def get_current_date():
    return datetime.now()


def get_current_time():
    return datetime.utcnow()


@bot.message_handler(commands=['date'])
def date(message):
    app.logger.debug("'date' command detected")
    current_date = "{:%a, %d %B %Y}".format(get_current_date())
    bot.reply_to(message, current_date)


@bot.message_handler(commands=['time'])
def time(message):
    app.logger.debug("'time' command detected")

    wib = 7 * 60 * 60
    base_utc = datetime(1970, 1, 1)
    now_utc = get_current_time()

    gmt_time = now_utc - base_utc
    gmt_time = gmt_time.total_seconds()
    gmt_time = gmt_time + wib

    wib_time = datetime.fromtimestamp(mktime(gmtime(gmt_time)))
    time_text = "{:%I:%M %p (GMT+7)}".format(wib_time)
    bot.reply_to(message, time_text)


@bot.message_handler(commands=['top_posters'])
def top_posters(message):
    response = 'Top 5 Posters:\n'
    app.logger.debug("'top_posters' command detected")

    if message.chat.type == 'private':
        bot.reply_to(message, "This command is only available for group chats!")

    elif message.chat.type == 'group':
        try:
            chat_messages = message_dic[message.chat.id]
            chat_total_mess = total_messages[message.chat.id]
            dic = sorted(chat_messages.items(), key=operator.itemgetter(1))
            for i, (name, count) in enumerate(reversed(dic[-5:])):
                response += '{}. {} ({:.2%})\n'.format(i+1, name, (count/chat_total_mess))
            bot.reply_to(message, response)

        except KeyError:
            bot.reply_to(message, 'No messages logged. Start chatting first!')


@bot.message_handler(func=_lyric_search_command)
def lyricsearch(message):
    app.logger.debug("'lyricsearch' command detected")
    cmd_len = len('/lyricsearch ')
    lyrics = message.text[cmd_len:]
    app.logger.debug('lyrics = {}'.format(lyrics))
    bot.reply_to(message, lyric_search(lyrics))


@bot.message_handler(func=_is_zodiac_command)
def zodiac(message):
    if message.text == '/zodiac':
        prompt_str = 'Please input the date in yyyy-mm-dd format, e.g. 1998-05-02'
        bot.reply_to(message, prompt_str)
    else:
        app.logger.debug("'zodiac' command detected")
        _, date_str = message.text.split(' ')
        _, month, day = _parse_date(date_str)
        app.logger.debug('month = {}, day = {}'.format(month, day))
        bot.reply_to(message, lookup_zodiac(month, day))


@bot.message_handler(func=_is_shio_command)
def shio(message):
    if message.text == '/shio':
        prompt_str = 'Please input the date in yyyy-mm-dd format, e.g. 1998-05-02'
        bot.reply_to(message, prompt_str)
    else:
        app.logger.debug("'shio' command detected")
        _, date_str = message.text.split(' ')
        year, _, _ = _parse_date(date_str)
        app.logger.debug('year = {}'.format(year))
        bot.reply_to(message, lookup_chinese_zodiac(year))


@bot.message_handler(func=_is_definisi_command)
def definisi(message):
    app.logger.debug("'definisi' command detected")
    word_list = message.text.split(' ')
    word = _parse_search_term(word_list)
    app.logger.debug('article = {}'.format(word))
    bot.reply_to(message, lookup_definisi(word))


@bot.message_handler(commands=['plants'])
def plants(message):
    app.logger.debug("'plants' command detected")
    bot.reply_to(message, lookup_plants_trivia())


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


@bot.message_handler(regexp=r'\w')
def get_messages(message):
    app.logger.debug("'get_message' handler detected")
    global message_dic
    global total_messages

    if message.chat.type == 'group':
        name = str(message.from_user.first_name)
        chat_id = message.chat.id
        try:
            message_dic[chat_id][name] += 1
        except KeyError:
            message_dic[chat_id][name] = 1
        total_messages[chat_id] += 1


def _parse_search_term(text):
    ret = text[1:]
    parse_word = " ".join(ret)
    return parse_word


def _parse_date(text):
    return tuple(map(int, text.split('-')))


@bot.message_handler(func=_is_chant_command)
def chant(message):
    app.logger.debug("'chant' command detected")
    bot.reply_to(message, generate_chant())
