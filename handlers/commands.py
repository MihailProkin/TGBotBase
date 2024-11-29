from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import keyboards.reply_kb as rk
import keyboards.inline_kb as ik

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот шаблон, можешь изменить мой код как тебе удобно!", reply_markup=rk.reply_start)