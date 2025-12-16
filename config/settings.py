import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class BotConfig:
    token: str
    group: str
    group_id: str


def load_config() -> BotConfig:
    token = os.getenv("TOKEN")
    group = os.getenv("GROUP")
    group_id = os.getenv("GROUP_ID")

    if not token:
        raise ValueError("Токен не задан в .env файле!")

    return BotConfig(token=token, group=group, group_id=group_id)

config = load_config()

TOKEN = config.token
GROUP = config.group
GROUP_ID = config.group_id
