from aiogram import Router, F # Импорт роуетра и фильтра
from aiogram.types import CallbackQuery, Message # Импорт типа данных месседж и каллбек
from aiogram.fsm.state import State, StatesGroup # Импорт для класса состояний
from aiogram.fsm.context import FSMContext # Импорт для типа данных классов
from aiogram.types import ReplyKeyboardRemove

import keyboards.reply_kb as rk
import keyboards.inline_kb as ik

call_router = Router()

@call_router.message(F.text == "Переключиться на inline клавиатуру")
async def reply_keyboard(message: Message):
    await message.answer("Переключаю", reply_markup=ReplyKeyboardRemove())
    await message.answer("Текст после нажатия на reply клавиатуру", reply_markup=ik.inline_start)
    
@call_router.callback_query(F.data == 'reply_kb')
async def inline_keyboard(callback: CallbackQuery):
    await callback.answer("Переключаю")
    await callback.message.answer("Текст после нажатия на inline клавиатуру", reply_markup=rk.reply_start)