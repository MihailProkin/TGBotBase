from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


reply_start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Переключиться на inline клавиатуру")]
], resize_keyboard=True)