import re
from __future__ import division

from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac



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

#TODO
def _is_compute_command(message):
    regexp = r'/compute'
    return re.match(regexp, message.text) is not None
    
#TODO
#use eval, what if not decimal?? ask around!
#if not math expression?? ->NameError
#breakitdown?? compute is command, take it out
#use search?
#pake try except aja ntar

@bot.message_handler(func=_is_compute_command)
def compute(message):
    return eval(message)
    pass

##do i really understand this tho
##if '/compute' in message:
##    head, sep, tail = message.partition('/')
##    input_nums = tail.replace('compute','')
##    input_nums = input_nums.replace('\'','')
##    finalexp = shlex.split(input_nums)
##    exp = finalexp[0]
##    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
##    error = 'Don\'t add alphabet in between please. for example do, /compute 2+2-5(4+8)'
##    if not exp:
##        bot.sendMessage(chat_id=chat_id,text='it is not a math expression.')
##    elif re.search('[a-zA-Z]', exp):
##        bot.sendMessage(chat_id=chat_id,text=error)
##    else:
##        bot.sendMessage(chat_id=chat_id,text=compute(exp))
##


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


def _parse_date(text):
    return tuple(map(int, text.split('-')))
