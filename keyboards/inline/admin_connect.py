from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


admin_msg_menu = InlineKeyboardMarkup(row_width=1)
admin_check = InlineKeyboardButton(text="📞 Foydalanuvchi bilan a'loqaga chiqilmagan", callback_data="check")
admin_msg_menu.insert(admin_check)

admin_msg_menu_2 = InlineKeyboardMarkup(row_width=1)
admin_checked = InlineKeyboardButton(text="✅ A'loqa o'rnatildi", callback_data="checked")
admin_msg_menu_2.insert(admin_checked)
