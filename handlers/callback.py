from aiogram import Router, F # Импорт роуетра и фильтра
from aiogram.types import CallbackQuery, Message # Импорт типа данных месседж и каллбек
from aiogram.fsm.state import State, StatesGroup # Импорт для класса состояний
from aiogram.fsm.context import FSMContext # Импорт для типа данных классов

call_router = Router()
