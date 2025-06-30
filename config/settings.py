import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    group: str

def load_config() -> BotConfig:
    load_dotenv()


    token = os.getenv("TELEGRAM_TOKEN")
    group = os.getenv("TELEGRAM_GROUP")

    if not token:
        raise ValueError("Токен не задан в .env файле!")

    return BotConfig(token=token, group=group)


# Загружаем конфиг и получаем токен
config = load_config()

TOKEN = config.token
GROUP = config.group
