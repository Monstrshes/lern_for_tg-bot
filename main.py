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


webapp_button = KeyboardButton(text='Start Web App', web_app=WebAppInfo(url='https://ru.wiktionary.org/wiki/%D0%B8%D0%B4%D0%B8_%D0%BD%D0%B0_%D1%85%D1%83%D0%B9'))

kb_builder= ReplyKeyboardBuilder()

# Добавляем кнопки в билдер
kb_builder.row(webapp_button, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='show_web'))
async def process_start_command(message: Message):
    await message.answer(
        text='Переходи по ссылке',
        reply_markup=keyboard
    )
if __name__ == '__main__':
    dp.run_polling(bot)