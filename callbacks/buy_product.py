from AsyncPayments.cryptoBot import AsyncCryptoBot

from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from data.database import get_value_from_json
from config import PRICE_PATH, CRYPTO_BOT_TOKEN

router = Router()


@router.callback_query(F.data.startswith("buy_"))
async def start_buy(call: CallbackQuery, bot: Bot):
    cryptoBot = AsyncCryptoBot(CRYPTO_BOT_TOKEN)

    prod_key = call.data.split("buy_")[-1]

    prod_price = get_value_from_json(PRICE_PATH, prod_key)

    order_crypto_bot = await cryptoBot.create_invoice(
        prod_price, currency_type="crypto", asset="USDT"
    )

    kb_btns = [
        [InlineKeyboardButton(text="🔗 Оплатить", url=order_crypto_bot.pay_url)],
        [
            InlineKeyboardButton(
                text="✅ Оплатил", callback_data=f"paid_{order_crypto_bot.invoice_id}"
            )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_btns)

    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"💸 Нажмите на кнопку оплатить, потом подтвердите оплату",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
