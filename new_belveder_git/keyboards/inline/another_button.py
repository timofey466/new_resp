from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import my_callback

remember = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                              text='да',
                                              callback_data=my_callback.new(item_name='off_course'))
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='нет',
                                            callback_data=my_callback.new(item_name='oy_no')
                                        )
                                    ]
                                ])