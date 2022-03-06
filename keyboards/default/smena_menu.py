from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

smena_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏞 Ertalabki oraliq(6:00 - 11:00)"),
            KeyboardButton(text="🌄 Kechki oraliq(13:00 - 18:00)"),
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ],
    ],
    resize_keyboard=True
)