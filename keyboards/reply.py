from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def register():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Register")]
        ],
        resize_keyboard=True
    )

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Profilim"), KeyboardButton(text="Ish topish")]
        ],
        resize_keyboard=True
    )

def job_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Online ish"), KeyboardButton(text="Offline ish")],
            [KeyboardButton(text="Orqaga ⬅️")]
        ],
        resize_keyboard=True
    )

def start_reply_admin():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Profilim"),KeyboardButton(text="Ish topish")],
            [KeyboardButton(text="Admin panel")]
        ],
        resize_keyboard=True
    )

def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="users")]
        ]
    )