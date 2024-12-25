import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN # Импортируем токен из файла config.py
from handlers.commands import router # Импортируем роутер из commands
from handlers.callback import call_router # Импортируем роутер из callback
from middlewares.localization_middleware import LanguageMiddleware

async def main(): # Основная функция
    try:
        token = BOT_TOKEN
        bot = Bot(token) 
        dp = Dispatcher()
        
        dp.message.middleware(LanguageMiddleware())
        dp.callback_query.middleware(LanguageMiddleware())
        
        dp.include_router(router)
        dp.include_router(call_router)
        
        print("Bot Start")
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"There is an Esception {ex}")
        
if __name__ == '__main__': # Условие для запуска асинхронной функции
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")