from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher()

button1 = KeyboardButton(text='Кнопка 1')
button2 = KeyboardButton(text='Кнопка 2')
button3 = KeyboardButton(text='Кнопка 3')
button4 = KeyboardButton(text='Кнопка 4')
button5 = KeyboardButton(text='Кнопка 5')
button6 = KeyboardButton(text='Кнопка 6')
button7 = KeyboardButton(text='Кнопка 7')
button8 = KeyboardButton(text='Кнопка 8')
button9 = KeyboardButton(text='Кнопка 9')

keyboard1 = ReplyKeyboardMarkup(keyboard=[
    [button1, button1],
    [button3, button4],
    [button5, button6],
    [button7, button8],
    [button9]

],
resize_keyboard=True
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это твоя клавиатура', reply_markup=keyboard1)

if __name__ == '__main__':
    dp.run_polling(bot)