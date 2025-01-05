from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String
from typing import Optional
import os

# Создаем базу данных SQLite в папке проекта
DATABASE_URL = "sqlite+aiosqlite:///database/bot_db.sqlite"

# Создаем движок базы данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем фабрику сессий
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

# Модель пользователя
class User(Base):
    __tablename__ = "users"
    
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(32))
    language: Mapped[str] = mapped_column(String(2))

# Функции для работы с БД
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_user(user_id: int) -> Optional[User]:
    async with async_session() as session:
        return await session.get(User, user_id)

async def add_user(user_id: int, username: Optional[str], language: str):
    async with async_session() as session:
        user = User(user_id=user_id, username=username, language=language)
        session.add(user)
        await session.commit()

async def update_user_language(user_id: int, new_language: str):
    async with async_session() as session:
        user = await session.get(User, user_id)
        if user:
            user.language = new_language
            await session.commit()