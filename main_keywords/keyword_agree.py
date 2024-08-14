from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def ret_keyword_agree():
    rus_button_yes = KeyboardButton(text='Да')
    rus_button_no = KeyboardButton(text='Нет')
    rus_keyword_agree = ReplyKeyboardMarkup(keyboard=[[rus_button_yes], [rus_button_no]])
    return rus_keyword_agree
