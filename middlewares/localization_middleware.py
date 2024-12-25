from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from localization import strings, DEFAULT_LANGUAGE


class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # 1. Пытаемся определить язык из объекта Message
        user_language = event.from_user.language_code if event.from_user else None
        
        # 2. Проверяем, поддерживаем ли мы этот язык
        if not user_language or user_language not in strings:
            user_language = DEFAULT_LANGUAGE
        
        # 3. Сохраняем язык в data, чтобы им могли пользоваться хендлеры
        data["language"] = user_language
        
        # 4. Передаём управление дальше
        return await handler(event, data)
