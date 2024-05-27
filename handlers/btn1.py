from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == 'Button1')
async def btn1_fun(msg: Message):
    await msg.answer('You clicked on btn1')
