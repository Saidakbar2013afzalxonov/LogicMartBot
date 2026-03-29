from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.reply import job_menu
from keyboards.inline import online_jobs, offline_jobs

router = Router()

@router.message(F.text == "Ish topish")
async def job_menu_handler(msg: Message):
    await msg.answer("Ish turini tanlang:", reply_markup=job_menu())

@router.message(F.text == "Online ish")
async def online_ish(msg: Message):
    await msg.answer("Online ishlar ro'yxati:", reply_markup=online_jobs())

@router.message(F.text == "Offline ish")
async def offline_ish(msg: Message):
    await msg.answer("Offline ishlar ro'yxati:", reply_markup=offline_jobs())

@router.callback_query(F.data.startswith("online_"))
async def online_job_info(cb: CallbackQuery):
    if cb.data == "online_freelancer":
        await cb.message.edit_text(
            "Ish: Online Freelancer\nMaosh: 6,000,000 so'm\nJoy: Yashnobod tumani, 256-maktab"
        )
    elif cb.data == "online_teacher":
        await cb.message.edit_text(
            "Ish: Online O'qituvchi\nMaosh: 5,500,000 so'm\nJoy: Yashnobod tumani, 123-maktab"
        )
    await cb.answer()

@router.callback_query(F.data.startswith("offline_"))
async def offline_job_info(cb: CallbackQuery):
    if cb.data == "offline_office":
        await cb.message.edit_text(
            "Ish: Ofis ishchi\nMaosh: 4,500,000 so'm\nJoy: Yashnobod tumani, 12-ofis"
        )
    elif cb.data == "offline_shop":
        await cb.message.edit_text(
            "Ish: Do'kon kassir\nMaosh: 4,000,000 so'm\nJoy: Yashnobod tumani, 5-do'kon"
        )
    await cb.answer()