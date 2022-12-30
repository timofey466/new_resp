from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.оставил (-а) отзыв")
        ],
        [
            KeyboardButton(text='2.узнать условия получения бонуса')
        ],
        [
            KeyboardButton(text='3.возник вопрос / проблема')
        ],
        [
            KeyboardButton(text="Получить скрин")
        ],
        [
            KeyboardButton(text="Ответить")
        ]
    ],
    resize_keyboard=True
)

helps = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='отправить отзыв')
        ],
        [
            KeyboardButton(text='связь с менеджером')
        ]
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True

)
adminback = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад')
        ],
        [
            KeyboardButton(text="Ответить")
        ]
    ],
    resize_keyboard=True
)

new_adminback = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад')
        ],
        [
            KeyboardButton(text="Получить скрин")
        ]
    ],
    resize_keyboard=True
)

yes_or_not = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='да')
        ],
        [
            KeyboardButton(text='нет')
        ]
    ],
    resize_keyboard=True
)

free_question = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.оставил (-а) отзыв")
        ],
        [
            KeyboardButton(text='2.узнать условия получения бонуса')
        ],
        [
            KeyboardButton(text='3.возник вопрос / проблема')
        ]
    ],
    resize_keyboard=True
)
