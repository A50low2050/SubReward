from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class BotConfig:
    token: str
    group: str
    group_id: str


def load_config() -> BotConfig:
    token = '7019540848:AAEzxE2zA8AlV3VVQZ2iJAeLnRGSacFIJBE'
    group = 'beautyserviceb2b/1'
    group_id = '@beautyserviceb2b'

    if not token:
        raise ValueError("Токен не задан в .env файле!")

    return BotConfig(token=token, group=group, group_id=group_id)


# Загружаем конфиг и получаем токен
config = load_config()

TOKEN = config.token
GROUP = config.group
GROUP_ID = config.group_id
