import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import user_commands, btn1


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(user_commands.router, btn1.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
