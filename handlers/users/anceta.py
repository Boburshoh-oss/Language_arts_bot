from aiogram import types
from aiogram.dispatcher import FSMContext
from states.personal_data import PersonalData
from aiogram.types import ReplyKeyboardRemove, ContentType
from keyboards.default.start_menu import konatakt_button
from keyboards.default.course_menu import course_menu
from keyboards.default.language_menu import language_menu, level_menu,level_rus_menu
from keyboards.default.smena_menu import smena_menu
from loader import dp
import logging
import re
from keyboards.inline.yes_no import check_anceta,sent,royhatdan_otish
from keyboards.default.start_menu import menuStart
from aiogram.types import  CallbackQuery
from data.config import ADMINS
from keyboards.inline.admin_connect import admin_msg_menu,admin_msg_menu_2

@dp.message_handler(text_contains="ro'yhatdan o'tish")
async def enter_test(message:types.Message):
    await message.answer("To'liq familya, ism, sharifingizni kiriting:",reply_markup=ReplyKeyboardRemove())
    await PersonalData.full_name.set()

@dp.message_handler(state=PersonalData.full_name)
async def answer_full_name(message:types.Message,state:FSMContext):
    full_name = message.text
    
    await state.update_data(
        {"full_name":full_name}
    )
    await message.answer("Kontaktingizni yuboring",reply_markup=konatakt_button)
    await PersonalData.phone_number.set()

@dp.message_handler(state=PersonalData.phone_number)
async def answer_error_number(message:types.Message,state:FSMContext):
   
    x = re.findall('[0-9]+', message.text)
    x= ''.join(x)
    await state.update_data(
        {"phone_number":x}
    )
    await message.answer("qaysi kursimizga yozilmoqchisiz tanlang",reply_markup=course_menu)
    await PersonalData.course.set()

@dp.message_handler(state=PersonalData.phone_number,content_types=ContentType.CONTACT)
async def answer_phone_num(message:types.Contact,state:FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(
        {"phone_number":phone_number}
    )
    await message.answer("qaysi kursimizga yozilmoqchisiz tanlang",reply_markup=course_menu)
    await PersonalData.course.set()


@dp.message_handler(state=PersonalData.course,text_contains="Chet tili")
async def answer_choose_language(message:types.Message,state:FSMContext):
    await message.answer("Tillardan birini tanlang:",reply_markup=language_menu)
    
    # await PersonalData.level.set()

@dp.message_handler(state=PersonalData.course,text_contains="Ortga")
async def back_course(message:types.Message,state:FSMContext):
    await message.answer("qaysi kursimizga yozilmoqchisiz tanlang",reply_markup=course_menu)
    
@dp.message_handler(state=PersonalData.course)
async def answer_course(message:types.Message,state:FSMContext):
    course = message.text
    await state.update_data(
        {"course":course}
    )
    if "Ingliz tili" in course:
        await message.answer("Darajangizni belgilang:",reply_markup=level_menu)
        await PersonalData.level.set()
    elif "Rus tili" in course:
        await message.answer("Darajangizni belgilang:",reply_markup=level_rus_menu)
        await PersonalData.level.set()
        
    elif "Matematika" in course:
        await message.answer("qaysi smemada o'qimoqchisiz",reply_markup=smena_menu)
        await PersonalData.smena.set()

@dp.message_handler(state=PersonalData.level,text_contains="Ortga")
async def back_level(message:types.Message,state:FSMContext):
    await message.answer("Tillardan birini tanlang:",reply_markup=language_menu)
    await PersonalData.course.set()
    
@dp.message_handler(state=PersonalData.level)
async def answer_level(message:types.Message,state:FSMContext):
    level = message.text
    await state.update_data(
        {"level":level}
    )
    await message.answer("qaysi smemada o'qimoqchisiz",reply_markup=smena_menu)
    await PersonalData.smena.set()


# @dp.message_handler(state=PersonalData.course)
# async def answer_phone_num(message:types.Message,state:FSMContext):
#     course = message.text
    
#     await state.update_data(
#         {"course":course}
#     )
#     await message.answer("qaysi smemada o'qimoqchisiz")
#     await PersonalData.smena.set()
@dp.message_handler(state=PersonalData.smena,text_contains="Ortga")
async def answer_back_course(message:types.Message,state:FSMContext):
    data = await state.get_data()
    course = data.get("course")
    if "Ingliz tili" in course:
        await message.answer("Darajangizni belgilang:",reply_markup=level_menu)
        await PersonalData.level.set()
    elif "Rus tili" in course:
        await message.answer("Darajangizni belgilang:",reply_markup=level_rus_menu)
        await PersonalData.level.set()
    
    elif "Matematika" in course:
        await message.answer("qaysi kursimizga yozilmoqchisiz tanlang",reply_markup=course_menu)
        await PersonalData.course.set()
    
@dp.message_handler(state=PersonalData.smena)
async def answer_smena(message:types.Message,state:FSMContext):
    smena = message.text
    
    await state.update_data(
        {"smena":smena}
    )
    #Malumotlarni qayta o'qish
    data = await state.get_data()
    name = data.get("full_name")
    phone = data.get("phone_number")
    course_data = data.get("course")
    level = data.get("level")
    smena_data = data.get("smena")
    
    msg = "💬 Sizning malumotlaringiz to'g'rimi tasdiqlash tugmachasini bosing:\n"
    
    msg += f"✅ F.I.O - {name}\n"
    
    msg += f"📞 telfon raqamingiz - {phone}\n"
    
    msg += f"📚 Siz tanlagan kurs - {course_data}\n"
    
    if level is not None:
        msg += f"📈 Sizning darajangiz - {level}\n"
        
    msg += f"🕑 Kurs vaqti - {smena_data}\n"
    

    # print(admins_msg)
    await message.answer(msg,reply_markup=check_anceta)
    
    
    # await message.answer("qaysi smemada o'qimoqchisiz")
    # await PersonalData.smena.set()

@dp.callback_query_handler(state=PersonalData.smena,text="checked_anceta")
async def checked_anceta(call: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    name = data.get("full_name")
    phone = data.get("phone_number")
    course_data = data.get("course")
    level = data.get("level")
    smena_data = data.get("smena")
    # Oynada javob qaytaramiz
    admins_msg = "Yangi foydalanuvchi ro'yhatdan o'tdi:\n"
    admins_msg += f"✅ <b>F.I.O</b> - {name}\n"
    if "+" not in phone:
        admins_msg += f"📞 <b>telfon raqami</b> - +{phone}\n"
    else:
        admins_msg += f"📞 <b>telfon raqami</b> - {phone}\n"
    admins_msg += f"📚 <b>Kursi</b> - {course_data}\n"
    if level is not None:
        admins_msg += f"📈 <b>Darajasi</b> - {level}\n"
    admins_msg += f"🕑 <b>Kurs vaqti</b> - {smena_data}\n"
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, admins_msg,reply_markup=admin_msg_menu)
        except Exception as err:
            logging.exception(err)
    # print(call,"callbaaak")
    
    await call.message.edit_reply_markup(reply_markup=sent)
    await call.message.reply("Habaringiz adminlar tomonidan ko'rib chiqilmoqda...")
    # await call.message("muvaffaqiyatli ro'yhatdan o'tdingniz!",reply_markup=ReplyKeyboardRemove)
    await state.finish()
    await call.answer()

@dp.callback_query_handler(state=PersonalData.smena,text="error_anceta")
async def error_anceta(call: CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("Qaytadan start buyrug'i orqali ro'yxatdan o'ting... /start")
    # Oynada javob qaytaramiz
    await state.finish()
    await call.answer()

@dp.callback_query_handler(text="check")
async def connect_user(call: CallbackQuery):
    # Oynada javob qaytaramiz
    try:
        await call.message.edit_reply_markup(reply_markup=admin_msg_menu_2)
    except:
        pass
    await call.answer()

@dp.callback_query_handler(text="checked")
async def unconnect_user(call: CallbackQuery):
    # Oynada javob qaytaramiz

    try:
        await call.message.edit_reply_markup(reply_markup=admin_msg_menu)
    except:
        pass
    await call.answer()
