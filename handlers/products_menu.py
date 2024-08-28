from aiogram import Router, F
from aiogram.types import Message

from keyboards.user import get_main_menu
from keyboards.inline_user import get_products_menu
from data.database import add_user_if_not_exists
from config import DB_PATH

router = Router()


@router.message(F.text == "🛒 Товары")
async def products_menu(msg: Message):
    user_id = msg.from_user.id
    await add_user_if_not_exists(DB_PATH, user_id)

    kb = await get_products_menu()
    await msg.answer(
        text="🛒 Вы перешли в меню товаров",
        reply_markup=kb,
        parse_mode="html",
    )
