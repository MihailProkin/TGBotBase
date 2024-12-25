# Telegram Bot Template

---

## 📑 Table of Contents

- [English](#english)
  - [📋 Description](#-description)
  - [🛠️ Features](#-features)
  - [🏗️ Project Structure](#-project-structure)
  - [🚀 Installation and Launch](#-installation-and-launch)
  - [🧰 Dependencies](#-dependencies)
  - [🌟 How to Use](#-how-to-use)
  - [🛡️ Security](#-security)
  - [📜 License](#-license)
  
- [Українською](#українською)
  - [📋 Опис](#-опис)
  - [🛠️ Функціонал](#-функціонал)
  - [🏗️ Структура проекту](#-структура-проекту)
  - [🚀 Встановлення та запуск](#-встановлення-та-запуск)
  - [🧰 Залежності](#-залежності)
  - [🌟 Як використовувати](#-як-використовувати)
  - [🛡️ Безпека](#-безпека)
  - [📜 Ліцензія](#-ліцензія)
  
- [Русский](#русский)
  - [📋 Описание](#-описание)
  - [🛠️ Функционал](#-функционал)
  - [🏗️ Структура проекта](#-структура-проекта)
  - [🚀 Установка и запуск](#-установка-и-запуск)
  - [🧰 Зависимости](#-зависимости)
  - [🌟 Как использовать](#-как-использовать)
  - [🛡️ Безопасность](#-безопасность)
  - [📜 Лицензия](#-лицензия)

---

## English

### 📋 Description

This project provides a template for quickly creating a Telegram bot using the [Aiogram](https://docs.aiogram.dev/) library.

### 🛠️ Features

- Command handling (e.g., `/start`, `/help`).
- Support for inline keyboards.
- Simple database setup.
- Organized project structure.
- Use of `.env` for storing sensitive data.

### 🏗️ Project Structure

```
TGBotBase/
├── bot.py                          # Main file to run the bot
├── handlers/                       # Command and event handlers
│   ├── commands.py                 # Example command handler
│   ├── callback.py                 # Example callback query handler
│   └── handlers_func.py            # Additional handlers
├── keyboards/                      # Telegram keyboard definitions
│   ├── inline.py                   # Inline keyboards
│   └── reply.py                    # Reply keyboards
├── database/                       # Database files
│   └── database.py                 # Database connection file
├── middlewares/                    # Middleware storage
│   └── localization_middleware.py  # Localization middleware
├── locales/                        # Localization folder
│   └── locale.json                 # Localization file
├── config.py                       # For storing the token and more...
├── .env                            # Environment variables (Better to use instead of config.py)
├── requirements.txt                # List of dependencies
├── .gitignore                      # Files and folders excluded from Git
├── LICENSE                         # License
└── README.md                       # Project description
```

### 🚀 Installation and Launch

1. Clone the repository:
   ```bash
   git clone https://github.com/V0L1ER/TGBotBase.git
   cd TGBotBase
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file or use `config.py` and add your bot token:
   ```
   BOT_TOKEN=your_bot_token
   ```
   _If using `.env`_:

   Install the `dotenv` dependency:
   ```
   pip install python-dotenv
   ```
   
   In `bot.py`, import `dotenv` and `os`:
   ```python
   import os
   from dotenv import load_dotenv
   ```
   
   Then call the `load_dotenv` function:
   ```python
   load_dotenv()
   ```
   
   Assign the `token` variable the value from `os.getenv('BOT_TOKEN')`:
   ```python
   token = os.getenv('BOT_TOKEN')
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

### 🧰 Dependencies

- Python 3.10+
- [Aiogram](https://docs.aiogram.dev/) 3.7+
- Other dependencies listed in `requirements.txt`.

### 🌟 How to Use

- Modify files in the `handlers/` folder to add new commands and handlers.
- Configure keyboards in the `keyboards/` folder.
- Connect your database in the `database/` folder.
- Add Middleware for additional functionality in `middlewares/`.

### 🛡️ Security

Do not add your bot token and other sensitive data directly into the code. Use `.env` to store them securely.

### 📜 License

This project is distributed under the MIT license. See the `LICENSE` file for more details.

---

## Українською

### 📋 Опис

Цей проект надає шаблон для швидкого створення Telegram-бота з використанням бібліотеки [Aiogram](https://docs.aiogram.dev/).

### 🛠️ Функціонал

- Обробка команд (наприклад, `/start`, `/help`).
- Підтримка інлайн-клавіатур.
- Просте налаштування бази даних.
- Організована структура проекту.
- Використання `.env` для зберігання конфіденційних даних.

### 🏗️ Структура проекту

```
TGBotBase/
├── bot.py                          # Головний файл для запуску бота
├── handlers/                       # Обробники команд та подій
│   ├── commands.py                 # Приклад обробника команд
│   ├── callback.py                 # Приклад обробника callback-запитів
│   └── handlers_func.py            # Додаткові обробники
├── keyboards/                      # Визначення клавіатур Telegram
│   ├── inline.py                   # Інлайн-клавіатури
│   └── reply.py                    # Reply-клавіатури
├── database/                       # Файли бази даних
│   └── database.py                 # Файл для підключення до Бази Даних
├── middlewares/                    # Сховище Middleware
│   └── localization_middleware.py  # Middleware для локалізації
├── locales/                        # Папка з локалізацією
│   └── locale.json                 # Файл для локалізації
├── config.py                       # Для зберігання токена та іншого...
├── .env                            # Змінні середовища (краще використовувати замість config.py)
├── requirements.txt                # Список залежностей
├── .gitignore                      # Файли та папки, виключені з Git
├── LICENSE                         # Ліцензія
└── README.md                       # Опис проекту
```

### 🚀 Встановлення та запуск

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/V0L1ER/TGBotBase.git
   cd TGBotBase
   ```

2. Створіть та активуйте віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Для Linux/MacOS
   venv\Scripts\activate      # Для Windows
   ```

3. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```

4. Створіть файл `.env` або використовуйте `config.py` і додайте токен бота:
   ```
   BOT_TOKEN=ваш_токен_бота
   ```
   _Якщо використовуєте `.env`_:

   Встановіть залежність `dotenv`:
   ```
   pip install python-dotenv
   ```
   
   У файлі `bot.py` імпортуйте `dotenv` та `os`:
   ```python
   import os
   from dotenv import load_dotenv
   ```
   
   Потім викличте функцію `load_dotenv`:
   ```python
   load_dotenv()
   ```
   
   Присвойте змінній `token` значення `os.getenv('BOT_TOKEN')`:
   ```python
   token = os.getenv('BOT_TOKEN')
   ```

5. Запустіть бота:
   ```bash
   python bot.py
   ```

### 🧰 Залежності

- Python 3.10+
- [Aiogram](https://docs.aiogram.dev/) 3.7+
- Інші залежності вказані в `requirements.txt`.

### 🌟 Як використовувати

- Модифікуйте файли в папці `handlers/`, щоб додавати нові команди та обробники.
- Налаштовуйте клавіатури в папці `keyboards/`.
- Підключайте свою базу даних в папці `database/`.
- Додавайте Middleware для більшої функціональності в `middlewares/`.

### 🛡️ Безпека

Не додавайте токен бота та інші конфіденційні дані безпосередньо у код. Використовуйте `.env` для їх зберігання.

### 📜 Ліцензія

Цей проект розповсюджується під ліцензією MIT. Детальніше дивіться у файлі `LICENSE`.

---

## Русский

### 📋 Описание

Этот проект предоставляет шаблон для быстрого создания Telegram-бота с использованием библиотеки [Aiogram](https://docs.aiogram.dev/).

### 🛠️ Функционал

- Обработка команд (например, `/start`, `/help`).
- Поддержка инлайн-клавиатур.
- Простая настройка базы данных.
- Организованная структура проекта.
- Использование `.env` для хранения конфиденциальных данных.

### 🏗️ Структура проекта

```
TGBotBase/
├── bot.py                          # Главный файл для запуска бота
├── handlers/                       # Обработчики команд и событий
│   ├── commands.py                 # Пример обработчика команд
│   ├── callback.py                 # Пример обработчика callback-запросов
│   └── handlers_func.py            # Дополнительные обработчики
├── keyboards/                      # Определения клавиатур Telegram
│   ├── inline.py                   # Инлайн-клавиатуры
│   └── reply.py                    # Reply-клавиатуры
├── database/                       # Файлы базы данных
│   └── database.py                 # Файл для подключения к Базе Данных
├── middlewares/                    # Хранилище Middleware
│   └── localization_middleware.py  # Middleware для локализации
├── locales/                        # Папка с локализацией
│   └── locale.json                 # Файл для локализации
├── config.py                       # Для хранения токена и тд...
├── .env                            # Переменные окружения (Лучше использовать вместо config.py)
├── requirements.txt                # Список зависимостей
├── .gitignore                      # Файлы и папки, исключённые из Git
├── LICENSE                         # Лицензия
└── README.md                       # Описание проекта
```

### 🚀 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/V0L1ER/TGBotBase.git
   cd TGBotBase
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Для Linux/MacOS
   venv\Scripts\activate      # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` или используйте `config.py` и добавьте токен бота:
   ```
   BOT_TOKEN=ваш_токен_бота
   ```
   _Если используете `.env`_:

   Установите зависимость `dotenv`:
   ```
   pip install python-dotenv
   ```
   
   В файле `bot.py` импортируйте `dotenv` и `os`:
   ```python
   import os
   from dotenv import load_dotenv
   ```
   
   Затем вызовите функцию `load_dotenv`:
   ```python
   load_dotenv()
   ```
   
   Присвойте переменной `token` значение `os.getenv('BOT_TOKEN')`:
   ```python
   token = os.getenv('BOT_TOKEN')
   ```

5. Запустите бота:
   ```bash
   python bot.py
   ```

### 🧰 Зависимости

- Python 3.10+
- [Aiogram](https://docs.aiogram.dev/) 3.7+
- Другие зависимости указаны в `requirements.txt`.

### 🌟 Как использовать

- Модифицируйте файлы в папке `handlers/`, чтобы добавлять новые команды и обработчики.
- Настраивайте клавиатуры в папке `keyboards/`.
- Подключайте свою базу данных в папке `database/`.
- Добавляйте Middleware для большего функционала в `middlewares/`.

### 🛡️ Безопасность

Не добавляйте токен бота и другие конфиденциальные данные в код. Используйте `.env` для их хранения.

### 📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле `LICENSE`.


