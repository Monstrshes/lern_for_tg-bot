from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='button1_pressed'
)
button2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='button2_pressed'
)

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[button1],
                    [button2]]
)