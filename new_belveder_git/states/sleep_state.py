from aiogram.dispatcher.filters.state import StatesGroup, State


class get_message(StatesGroup):
    wait = State()
    admin_wait = State()
    photo_admin_wait = State()
    photo_with = State()
    what_error = State()
    new_wait = State()