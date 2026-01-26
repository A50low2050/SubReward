from dataclasses import dataclass
from typing import Optional

@dataclass
class MessageInputDTO:
    """
    DTO Message.
    """

    user_id: int
    first_name: str
    username: str
    message_id: int
    chat_id: int
    text: Optional[str]
    type: str
    command: Optional[str] = None
