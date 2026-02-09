from dataclasses import dataclass
from typing import Optional
from bot.user.models import User


@dataclass
class MessageInputDTO:

    user: User
    message_id: int
    chat_id: int
    text: Optional[str]
    type: str
    command: Optional[str] = None
