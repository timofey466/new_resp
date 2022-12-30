import asyncio
import datetime
import time

import schedule as schedule
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, CallbackQuery

from data.config import admins
from keyboards.default.local import back, question_list, adminback, new_adminback, yes_or_not, free_question
from keyboards.inline.another_button import remember
from keyboards.inline.callback_data import my_callback
from loader import dp, bot
from states.sleep_state import get_message
from utils.misc import rate_limit

user_text = []
user_chat_id = []
photo_user = []
photo_chat = []
ad = []
admin_chat = []
req = []
back_user = []


@rate_limit(limit=5)
@dp.message_handler(commands=['start'])
async def started(message: types.Message):
    if message.from_user.id in admins:
        await message.reply(
            "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
            "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
            "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
            "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
            "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
            "проблема",
            reply_markup=question_list)
    else:
        await message.reply(
            "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
            "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
            "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
            "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
            "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
            "проблема", reply_markup=free_question)




@rate_limit(limit=5)
@dp.message_handler(text='1.оставил (-а) отзыв')
async def qrcode(message: types.Message, state: FSMContext):
    await message.answer("Супер, спасибо тебе!😘\n\nВ таком случае, ждем 2 скриншота (твоего отзыва и заказа), "
                         "и 150 RUB очень скоро будут у тебя.\n\nВ Личном кабинете на сайте WB все оставленные отзывы "
                         "можно найти в разделе \"Профиль\" - \"Отзывы и вопросы\".\n❗️Чтобы вернуться в начало, "
                         "отправь \"1\"",
                         reply_markup=back)
    await message.reply("❗После отправки скриншота отправьте свои реквизиты для перевода денег❗")


@rate_limit(limit=10)
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def get_photograph(message: types.Message):
    photo_user.append(message.photo[-1].file_id)
    photo_chat.append(message.chat.id)
    await get_message.photo_with.set()


@rate_limit(limit=5)
@dp.message_handler(state=get_message.photo_with)
async def get_photo_caption(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        req.append(message.text)
    await state.finish()
    time.sleep(1)
    await message.reply("Мы получили ваше сообщение")
    for i in admins:
        await bot.send_message(chat_id=i, text="Пришёл новый скрин")



@rate_limit(limit=5)
@dp.message_handler(text='2.узнать условия получения бонуса')
async def knowbone(message: types.Message):
    await message.answer(
        "Для того, чтобы получить свой денежный бонус, тебе нужно оставить отзыв.\nРасскажи, что тебе понравилось в "
        "SHBNV: продукт, упаковка, сервис, доставка.\nПрикрепи фото (это по желанию, но нам будет приятно).\n\n❗️Обрати внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с тобой😉\n\nСледуй "
        "по пунктам, и у тебя все получится 🤍:\n\n1️⃣ Зайди в Личный кабинет\n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери "
        "товар SHBNV, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, "
        "чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и "
        "прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, отправь \"Назад\"", reply_markup=back)


@rate_limit(limit=5)
@dp.message_handler(text='3.возник вопрос / проблема')
async def error_helps(message: types.Message):
    await message.answer(
        "Опиши проблему, которая у тебя возникла. Менеджер SHBNV тебе поможет и ответит на все твои "
        "вопросы.\nОбезательно дождитесь сообщения \"Мы получили ваше сообщение\", иначе ваш запрос будет не "
        "получен\n\n❗️Чтобы вернуться в начало, отправь \"Назад\"",
        reply_markup=back)
    await get_message.wait.set()


@dp.message_handler(state=get_message.wait)
async def error_helps(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        user_text.append(message.text)
        user_chat_id.append(message.chat.id)
    await state.finish()
    time.sleep(1)
    await message.reply("Мы получили ваше сообщение")
    for i in admins:
        await bot.send_message(chat_id=i, text="сообщение от клиента")


@rate_limit(limit=5)
@dp.message_handler(text="Ответить")
async def error_helps(message: types.Message, state: FSMContext):
    try:
        if message.from_user.id in admins:
            await message.reply(user_text[0])
            user_text.remove(user_text[0])
    except Exception as eror:
        await message.reply("Проблем нет")
    await get_message.new_wait.set()


@dp.message_handler(state=get_message.new_wait)
async def error_helps(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        await bot.send_message(chat_id=user_chat_id[0], text=f'{message.text}')
        user_chat_id.remove(user_chat_id[0])


@rate_limit(limit=5)
@dp.message_handler(text="Получить скрин")
async def error_helps(message: types.Message, state: FSMContext):
    try:
        if message.from_user.id in admins:
            await bot.send_photo(chat_id=message.chat.id, photo=photo_user[0])
            await bot.send_message(chat_id=message.chat.id, text=req[0])
            await get_message.photo_admin_wait.set()
            async with state.proxy() as proxy:
                photo_user.remove(photo_user[0])
                req.remove(req[0])
                await message.reply("клиент всё сделал верно?", reply_markup=yes_or_not)
                await state.finish()
        elif message.from_user.id not in admins:
            await message.reply("Эта кнопка только для администраторов.Вы не имеете доступа к этой кнопке")
    except Exception as eror:
        await message.reply("Скринов нет")
        print(eror)


@rate_limit(limit=5)
@dp.message_handler(text="да")
async def backdoor(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Отлично", reply_markup=back)
    photo_chat.remove(photo_chat[0])


@rate_limit(limit=5)
@dp.message_handler(text="нет")
async def backdoor(message: types.Message):
    await message.answer("Что пользователь сделал не так?")
    await get_message.what_error.set()


@dp.message_handler(state=get_message.what_error)
async def error_helps(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        back_user.append(message.text)
    await state.finish()
    time.sleep(1)
    await message.reply("Мы получили ваше сообщение", reply_markup=back)
    await bot.send_message(chat_id=photo_chat[0], text=message.text)
    photo_chat.remove(photo_chat[0])


@rate_limit(limit=5)
@dp.message_handler(text="Назад")
async def backdoor(message: types.Message):
    if message.from_user.id in admins:
        await message.reply(
            "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
            "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
            "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
            "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
            "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
            "проблема",
            reply_markup=question_list)
    else:
        await message.reply(
            "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
            "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
            "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
            "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
            "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
            "проблема", reply_markup=free_question)
