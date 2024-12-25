from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import keyboards.reply_kb as rk
import keyboards.inline_kb as ik
from localization import get_string

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, language: str):
    await message.answer(text=get_string(language, "start-message"), reply_markup=rk.reply_start(language))