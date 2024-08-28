import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN, DB_PATH
from handlers import user_commands, products_menu
from data.database import initialize_db


async def main():
    await initialize_db(DB_PATH)

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(user_commands.router, products_menu.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
