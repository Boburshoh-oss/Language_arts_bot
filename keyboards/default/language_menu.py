from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Ingliz tili"),
            KeyboardButton(text="📚 Rus tili"),
        ],
        [
            KeyboardButton(text="◀️ Ortga")
        ],
    ],
    resize_keyboard=True
)

level_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Beginner"),
            KeyboardButton(text="Elementary"),
        ],
        [
            KeyboardButton(text="Pre intermediate"),
            KeyboardButton(text="Intermediate")
        ],
        [
            KeyboardButton(text="Upper intermediate")
        ],
        [
            KeyboardButton(text="◀️ Ortga")
        ],
    ],
    resize_keyboard=True
)

level_rus_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="So'zlashuv"),
            KeyboardButton(text="grammatika"),
        ],
        [
            KeyboardButton(text="Ummumiy rus tili")
        ],
        [
            KeyboardButton(text="◀️ Ortga")
        ],
    ],
    resize_keyboard=True
)