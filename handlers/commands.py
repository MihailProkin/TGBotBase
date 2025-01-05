from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import keyboards.reply_kb as rk
from localization import get_string
from database.database import add_user, get_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, language: str):
    user = await get_user(message.from_user.id)
    if not user:
        await add_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            language=language
        )
    
    await message.answer(
        text=get_string(language, "start-message"),
        reply_markup=rk.reply_start(language)
    )