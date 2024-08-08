from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def ret_keyword_agree(lang):
    if lang == 'rus':
        rus_button_yes = KeyboardButton(text='Да')
        rus_button_no = KeyboardButton(text='Нет')
        rus_keyword_agree = ReplyKeyboardMarkup(keyboard=[[rus_button_yes], [rus_button_no]])
        return rus_keyword_agree
    else:
        eng_button_yes = KeyboardButton(text='Yes')
        eng_button_no = KeyboardButton(text='No')
        eng_keyword_agree = ReplyKeyboardMarkup(keyboard=[[eng_button_yes], [eng_button_no]])
        return eng_keyword_agree