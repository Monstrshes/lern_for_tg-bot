from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.inline_keyboards import keyboard1

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Ничего не было нажато',
        reply_markup=keyboard1
    )

@router.callback_query(F.data.in_(['button1_pressed']))
async def process_inline_keyboard_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Была нажата БОЛЬШАЯ КНОПКА 1',
        reply_markup=keyboard1
    )

@router.callback_query(F.data.in_(['button2_pressed']))
async def process_inline_keyboard_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Была нажата БОЛЬШАЯ КНОПКА 2',
        reply_markup=keyboard1
    )