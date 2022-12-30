import logging
import time

import schedule
from aiogram import Dispatcher

from data.config import admins
from handlers.users.cripto import user_text
from loader import bot
from threading import Thread
num = []

async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе")

        except Exception as err:
            logging.exception(err)



