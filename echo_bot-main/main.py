from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
import logging
import asyncio
from set_menu.menu import ret_menu

logger = logging.getLogger(__name__)

dp = Dispatcher()

async def main():

    config: Config = load_config()
    tg_bot = Bot(token=config.tg_bot.token)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await ret_menu(tg_bot)

    format = '%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=format)

    await tg_bot.delete_webhook()
    await dp.start_polling(tg_bot)

asyncio.run(main())

