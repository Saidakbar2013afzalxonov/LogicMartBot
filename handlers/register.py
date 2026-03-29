from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.reply import main_menu, register
from states.register import RegisterState

router = Router()

@router.message(F.text == "Register")
async def register_start(msg: Message, state: FSMContext, db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer("Siz avval ro'yxatdan o'tgansiz.", reply_markup=main_menu())
    else:
        await msg.answer("Ismingizni kiriting:")
        await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def register_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Familyangizni kiriting:")
    await state.set_state(RegisterState.surename)

@router.message(RegisterState.surename)
async def register_surename(msg: Message, state: FSMContext):
    await state.update_data(surename=msg.text)
    await msg.answer("Yoshingizni kiriting:")
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def register_age(msg: Message, state: FSMContext):
    await state.update_data(age=int(msg.text))
    await msg.answer("Telefon raqamingizni kiriting:")
    await state.set_state(RegisterState.phone_number)

@router.message(RegisterState.phone_number)
async def register_phone(msg: Message, state: FSMContext, db):
    await state.update_data(phone_number=msg.text)
    data = await state.get_data()
    await db.add_user(msg.from_user.id, data["name"], data["surename"], data["age"], data["phone_number"])
    await msg.answer(
        f"Malumotlaringiz saqlandi:\nIsm: {data['name']}\nFamilya: {data['surename']}\nYosh: {data['age']}\nTelefon: {data['phone_number']}",
        reply_markup=main_menu()
    )
    await state.clear()