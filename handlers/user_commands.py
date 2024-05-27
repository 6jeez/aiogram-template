from aiogram import Router, F
from aiogram.types import Message

from keyboards.user import get_main_menu

router = Router()


@router.message(F.text == '/start')
async def start_func(msg: Message):
    kb = await get_main_menu()
    await msg.answer(text='Hi!', reply_markup=kb)
