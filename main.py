import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse

load_dotenv(dotenv_path='tokens.env')

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


def reply(chat_id, question):
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_countdown(parse(question), notify_progress, chat_id=chat_id, message_id=message_id, question=question)
    bot.create_timer(parse(question), wait, chat_id=chat_id, question=question)


def wait(chat_id, question):
    message = 'Время вышло!'
    bot.send_message(chat_id, message)


def notify_progress(secs_left, chat_id, message_id, question):
    message = render_progressbar(parse(question), secs_left, f'Осталось {secs_left} секунд!')
    bot.update_message(chat_id, message_id, message)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    bot = ptbot.Bot(TELEGRAM_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()