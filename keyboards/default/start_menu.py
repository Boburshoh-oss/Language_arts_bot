from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ ro'yhatdan o'tish")
        ],
    ],
    resize_keyboard=True 
)

konatakt_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Kontaktni ulashish",request_contact=True)
        ],
    ],
    resize_keyboard=True
)