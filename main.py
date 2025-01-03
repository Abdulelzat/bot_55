import asyncio
import logging
from bot_config import dp, bot, database
from handlers.other_massages import echo_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import randomfile
from handlers.review_dialog import review_router
from handlers.menu_management import menu_management_router
from handlers.dishes import menu_list_router

async def on_startup(bot):
    database.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(randomfile)
    dp.include_router(review_router)
    dp.include_router(menu_management_router)
    dp.include_router(menu_list_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())