from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    name = State()
    surename = State()
    age = State()
    phone_number = State()