from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

course_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📙 Chet tili"),
            KeyboardButton(text="📐 Matematika"),
        ],
    ],
    resize_keyboard=True
)