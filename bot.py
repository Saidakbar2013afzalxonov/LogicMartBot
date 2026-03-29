from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from config import config
from database.db import Database

from handlers.start import router as start_router
from handlers.register import router as register_router
from handlers.profile import router as profile_router
from handlers.jobs_callback import router as jobs_router

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    db = Database()
    await db.connection()
    dp["db"] = db

    dp.include_router(start_router)
    dp.include_router(register_router)
    dp.include_router(profile_router)
    dp.include_router(jobs_router)

    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())