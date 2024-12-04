from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types.web_app_info import WebAppInfo

env = Env()
env.read_env()

bot = Bot(env('BOT_TOKEN'))
dp = Dispatcher()


# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]
]

keyboard.append(KeyboardButton(text='7'))

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот твоя клавиатура',
        reply_markup=my_keyboard
    )
if __name__ == '__main__':
    dp.run_polling(bot)