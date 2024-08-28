from AsyncPayments.cryptoBot import AsyncCryptoBot

from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from data.database import get_value_from_json
from config import PRICE_PATH, CRYPTO_BOT_TOKEN

router = Router()


@router.callback_query(F.data.startswith("paid_"))
async def check_payment(call: CallbackQuery, bot: Bot):
    cryptoBot = AsyncCryptoBot(CRYPTO_BOT_TOKEN)

    payment_id = call.data.split("paid_")[-1]

    info_crypto_bot = await cryptoBot.get_invoices(invoice_ids=[payment_id], count=1)

    if info_crypto_bot[0].status == "paid":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="✅ Оплачено",
        )
    elif info_crypto_bot[0].status == "active":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="❌ Вы не оплатили",
        )
