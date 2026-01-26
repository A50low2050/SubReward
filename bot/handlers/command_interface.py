from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from bot.user.domain.entities.user import User


class CommandsInterface(ABC):

    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def handle(self, user: User):
        pass

    @abstractmethod
    def get_reply_message_data(self):
        pass

    @abstractmethod
    def _get_text_message(self) -> str:
        pass

    @abstractmethod
    def _get_reply_keyboards(self) -> list:
        pass

    @abstractmethod
    def _get_parse_mode(self) -> str:
        pass
