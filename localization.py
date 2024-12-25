import json
import os

DEFAULT_LANGUAGE = "en"

def load_strings() -> dict:
    with open("./locales/locale.json", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Глобальная переменная, где лежат все локализации
strings = load_strings()

def get_string(language: str, key: str) -> str:
    try:
        return strings[language][key]
    except KeyError:
        # Например, возвращаем 'error' из словаря
        return strings[language].get("error", "Error")