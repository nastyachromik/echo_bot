from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router

router = Router()

@router.message()
async def echo_func(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())