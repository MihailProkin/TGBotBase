from aiogram import Router, F # Импорт роуетра и фильтра
from aiogram.types import CallbackQuery, Message # Импорт типа данных месседж и каллбек
from aiogram.fsm.state import State, StatesGroup # Импорт для класса состояний
from aiogram.fsm.context import FSMContext # Импорт для типа данных классов
from aiogram.types import ReplyKeyboardRemove

import keyboards.reply_kb as rk
import keyboards.inline_kb as ik
from localization import get_string

call_router = Router()

@call_router.message(F.text.contains("inline"))
async def get_reply_kb(message: Message, language: str):
    await message.answer(get_string(language, "callback-answer"), reply_markup=ReplyKeyboardRemove())
    await message.answer(get_string(language, "press-reply"), reply_markup=ik.inline_start(language))
    
@call_router.callback_query(F.data == 'reply_kb')
async def get_inline_kb(callback: CallbackQuery, language: str):
    await callback.answer(get_string(language, "callback-answer"))
    await callback.message.answer(
        get_string(language, "press-inline"), 
        reply_markup=rk.reply_start(language)
    )