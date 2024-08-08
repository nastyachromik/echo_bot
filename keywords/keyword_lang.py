from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_rus = KeyboardButton(text='Русский')
button_eng = KeyboardButton(text='English')

keyword = ReplyKeyboardMarkup(keyboard=[[button_rus], [button_eng]])
