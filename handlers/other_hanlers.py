from aiogram.types import Message
from aiogram import Router
from ..lexicon import *

#Инициализируем роутер
router = Router()

#Эхо - функция
@router.message()
async def process_eho_command(message:Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
