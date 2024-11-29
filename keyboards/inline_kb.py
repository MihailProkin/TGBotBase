from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Переключиться на reply клавиатуру", callback_data='reply_kb')]
])