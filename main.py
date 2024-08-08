from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers

dp = Dispatcher()
async def main():
    config: Config = load_config()
    global tg_bot
    tg_bot = Bot(token=config.tg_bot.token)
    dp.include_router(user_handlers.router)
    #dp.include_router(other_handlers.router)

if __name__ == '__main__':
    dp.run_polling()

