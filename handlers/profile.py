from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "Profilim")
async def profilim(msg: Message, db):
    user = await db.get_user(msg.from_user.id)
    if user:
        await msg.answer(
            f"Sizning profilingiz:\nIsm: {user['name']}\nFamilya: {user['surename']}\nYosh: {user['age']}\nTelefon: {user['phone']}"
        )
    else:
        await msg.answer("Siz hali ro'yxatdan o'tmagansiz. Iltimos Register tugmasini bosing.")