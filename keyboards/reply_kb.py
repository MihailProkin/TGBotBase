from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from localization import get_string

def reply_start(language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_string(language, "reply-start"))]
        ],
        resize_keyboard=True  # Дополнительные параметры передаются отдельно
    )