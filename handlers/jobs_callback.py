from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data.startswith("online_"))
async def online_job_info(cb: CallbackQuery):
    if cb.data == "online_freelancer":
        await cb.message.edit_text("Ish: Online Freelancer\nTavsif: Uyda ishlash, mustaqil loyiha asosida\nMaosh: 6,000,000 so'm")
    elif cb.data == "online_teacher":
        await cb.message.edit_text("Ish: Online O'qituvchi\nTavsif: Internet orqali dars berish\nMaosh: 5,500,000 so'm")
    await cb.answer()

@router.callback_query(F.data.startswith("offline_"))
async def offline_job_info(cb: CallbackQuery):
    if cb.data == "offline_office":
        await cb.message.edit_text("Ish: Ofis ishchi\nJoy: Yashnobod tumani, 12-ofis\nMaosh: 4,500,000 so'm")
    elif cb.data == "offline_shop":
        await cb.message.edit_text("Ish: Do'kon kassir\nJoy: Yashnobod tumani, 5-do'kon\nMaosh: 4,000,000 so'm")
    await cb.answer()