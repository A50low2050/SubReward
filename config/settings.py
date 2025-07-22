import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    group: str
    bot: str

def load_config() -> BotConfig:
    load_dotenv()


    token = os.getenv("TELEGRAM_TOKEN")
    group = os.getenv("TELEGRAM_GROUP")
    bot = os.getenv("TELEGRAM_BOT")

    if not token:
        raise ValueError("Токен не задан в .env файле!")

    return BotConfig(token=token, group=group, bot=bot)


# Загружаем конфиг и получаем токен
config = load_config()

TOKEN = config.token
GROUP = config.group
BOT = config.bot
