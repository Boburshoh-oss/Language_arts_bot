import logging

from data.config import CHANNELS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_menu import menuStart
from keyboards.inline.subscription import check_button
from loader import dp, bot
from utils.misc.subscription import check
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Salom, {message.from_user.full_name}! Ro'yhatdan o'tish uchun avval kanallarga obuna bo'ling:\n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)

@dp.callback_query_handler(text="check_subs")
async def checker(call:types.CallbackQuery):
    await call.answer()
    result = str()
    checks = 0
    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id,
                             channel=channel)
        channel = await bot.get_chat(channel)
        
        if status:
            result += f"✅ <b>{channel.title}</b> Kanaliga obuna bo'lgansiz ro'yhatdan o'tish uchun <b>Ro'yhatdan o'tishga</b> bosing"
            checks += 1
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <b>{channel.title}</b> Kanaliga obuna bo'lmagansiz."
                       f"<a href='{invite_link}'>Obuna bo'ling</a> va qaytadan tekshiring\n\n")
    if checks==1:
        await call.message.answer(result,disable_web_page_preview=True,reply_markup=menuStart)
    else:
        await call.message.answer(result,disable_web_page_preview=True,reply_markup=ReplyKeyboardRemove())