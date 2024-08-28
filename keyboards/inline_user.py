from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_products_menu():
    kb = []

    kb.append(
        [
            InlineKeyboardButton(text="Купить 1K", callback_data="buy_1k"),
        ]
    )

    kb.append(
        [
            InlineKeyboardButton(text="Купить 2K", callback_data="buy_2k"),
        ]
    )

    kb.append(
        [
            InlineKeyboardButton(text="Купить 3K", callback_data="buy_3k"),
        ]
    )

    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=kb)

    return keyboard
