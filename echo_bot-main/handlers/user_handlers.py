from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import Router, F
from lexicon.lexicon import commands_rus
from main_keywords.keyword_agree import ret_keyword_agree

router = Router()


@router.message(Command(commands=['start']))
async def start_func(message: Message):
    await message.answer(f'{commands_rus["start"]}', reply_markup=ret_keyword_agree())

@router.message(F.text.lower().strip().in_(['да']))
async def agree_func(message: Message):
    await message.answer(text=commands_rus['yes'], reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower().strip().in_(['нет']))
async def disagree_func(message: Message):
    await message.answer(text=commands_rus['no'], reply_markup=ReplyKeyboardRemove())

@router.message(Command(commands=['help']))
async def help_func(message: Message):
    await message.answer(text=commands_rus['help'])

