from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    full_name = State()
    phone_number = State()
    course = State()
    level = State()
    smena = State()