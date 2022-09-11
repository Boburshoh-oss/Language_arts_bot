from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_anceta = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅",callback_data="checked_anceta"),
        InlineKeyboardButton(text="❌",callback_data="error_anceta"),
    ]]
)

sent = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ sent",callback_data="checked_anceta"),
        
    ]]
)

royhatdan_otish = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Ro'yhatdan o'tish",callback_data="ro'yhatdan o'tish"),
        
    ]]
)