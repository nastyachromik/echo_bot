from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import Router, F
from keywords.keyword_lang import keyword
from keywords.keyword_agree import ret_keyword_agree
from lexicon.lexicon import languages

router = Router()
user_lang = None
user_stat = False

@router.message(Command(commands=['start']))
async def start_func(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         f'Напиши мне любое сообщение, а я повторю\n!'
                         f'Но для начала выберите язык', reply_markup=keyword)

@router.message(F.text.lower().strip().in_(['русский', 'english']))
async def continue_func(message: Message):
    if message.text == 'русский':
        user_lang = 'rus'
    else:
        user_lang = 'eng'
    await message.answer(text=languages[user_lang]['start'], reply_markup=ret_keyword_agree(user_lang))

@router.message(F.text.lower().strip().in_(['да', 'yes']))
async def agree_func(message: Message):
    user_stat = True
    await message.answer(text=languages[user_lang]['yes'], reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower().strip().in_(['нет', 'no']))
async def disagree_func(message: Message):
    global user_stat
    user_stat = False
    await message.answer(text=languages[user_lang]['no'], reply_markup=ReplyKeyboardRemove())

@router.message(Command(commands=['lang']))
async def lang_func(message: Message):
    await message.answer(text=languages[user_lang]['choose_lang'], reply_markup=keyword)

@router.message(Command(commands=['help']))
async def help_func(message: Message):
    await message.answer(text=languages[user_lang]['help'])

@router.message()
async def echo_func(message: Message):
    if user_stat:
        await message.answer(message.text, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=languages[user_lang]['other'], reply_markup=ReplyKeyboardRemove())