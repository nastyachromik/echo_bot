from aiogram.types import BotCommand
from aiogram import Bot
from lexicon.lexicon import menu_commands

async def ret_menu(bot:Bot):
    menu = [BotCommand(command=command, description=des) for command,des in menu_commands.items()]
    await bot.set_my_commands(menu)