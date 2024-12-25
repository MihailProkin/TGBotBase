# Telegram Bot Template

Certainly! Below is your `README.md` file translated into **English**, **Ukrainian**, and **Russian**, each section equipped with anchor links for easy navigation on GitHub.

---

# TGBotBase

## 📑 Table of Contents

- [English](#english)
  - [📋 Description](#%F0%9F%93%8B-description)
  - [🛠️ Features](#%F0%9F%9B%A0-features)
  - [🏗️ Project Structure](#%F0%9F%8F%97-project-structure)
  - [🚀 Installation and Launch](#%F0%9F%9A%80-installation-and-launch)
  - [🧰 Dependencies](#%F0%9F%A7%AE-dependencies)
  - [🌟 How to Use](#%F0%9F%8C%9F-how-to-use)
  - [🛡️ Security](#%F0%9F%9B%A1-security)
  - [📜 License](#%F0%9F%93%9C-license)
  
- [Українською](#українською)
  - [📋 Опис](#%F0%9F%93%8B-%D0%BE%D0%BF%D0%B8%D1%81)
  - [🛠️ Функціонал](#%F0%9F%9B%A0-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB)
  - [🏗️ Структура проекту](#%F0%9F%8F%97-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%83)
  - [🚀 Встановлення та запуск](#%F0%9F%9A%80-%D0%B2%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F-%D1%82%D0%B0-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
  - [🧰 Залежності](#%F0%9F%A7%AE-%D0%B7%D0%B0%D0%BB%D0%B5%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%96)
  - [🌟 Як використовувати](#%F0%9F%8C%9F-%D1%8F%D0%BA-%D0%B2%D0%B8%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B2%D0%B0%D1%82%D0%B8%D1%8E%D1%82%D0%B8)
  - [🛡️ Безпека](#%F0%9F%9B%A1-%D0%B1%D0%B5%D0%B7%D0%BF%D0%B5%D0%BA%D0%B0)
  - [📜 Ліцензія](#%F0%9F%93%9C-%D0%BB%D1%96%D1%86%D0%B5%D0%BD%D0%B7%D1%96%D1%8F)
  
- [Русский](#русский)
  - [📋 Описание](#%F0%9F%93%8B-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5)
  - [🛠️ Функционал](#%F0%9F%9B%A0-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB)
  - [🏗️ Структура проекта](#%F0%9F%8F%97-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
  - [🚀 Установка и запуск](#%F0%9F%9A%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B8-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
  - [🧰 Зависимости](#%F0%9F%A7%AE-%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8)
  - [🌟 Как использовать](#%F0%9F%8C%9F-%D0%BA%D0%B0%D0%BA-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F)
  - [🛡️ Безопасность](#%F0%9F%9B%A1-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
  - [📜 Лицензия](#%F0%9F%93%9C-%D0%BB%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F)

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
│   └── localization_middleware.py   # Localization middleware
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
│   └── localization_middleware.py   # Middleware для локалізації
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
│   └── localization_middleware.py   # Middleware для локализации
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

---

## 📌 Notes

- **Environment Variables:** It's recommended to use the `.env` file for sensitive information like bot tokens instead of hardcoding them in `config.py`.
- **Localization:** Ensure that the `localization_middleware.py` correctly injects the `language` variable into your handlers.
- **Dependencies:** Keep your dependencies updated by regularly checking the `requirements.txt` file.

---

Feel free to customize each section further to better fit your project's specifics!

