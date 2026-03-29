from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply import main_menu, job_menu
from keyboards.inline import online_jobs_keyboard, offline_jobs_keyboard

router = Router()

@router.message(F.text == "/start")
async def start(msg: Message):
    await msg.answer("Xush kelibsiz! Iltimos ro'yxatdan o'ting:", reply_markup=register())

@router.message(F.text == "Ish topish")
async def job_menu_handler(msg: Message):
    await msg.answer("Ish turini tanlang:", reply_markup=job_menu())

@router.message(F.text == "Online ish")
async def online_job(msg: Message):
    await msg.answer("Online ishlar ro'yxati:", reply_markup=online_jobs_keyboard())

@router.message(F.text == "Offline ish")
async def offline_job(msg: Message):
    await msg.answer("Offline ishlar ro'yxati:", reply_markup=offline_jobs_keyboard())