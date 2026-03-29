from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def online_jobs_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Freelancer", callback_data="online_freelancer")],
            [InlineKeyboardButton(text="Online O'qituvchi", callback_data="online_teacher")]
        ]
    )

def offline_jobs_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ofis ishchi", callback_data="offline_office")],
            [InlineKeyboardButton(text="Do'kon kassir", callback_data="offline_shop")]
        ]
    )