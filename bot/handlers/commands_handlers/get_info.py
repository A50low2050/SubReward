from sqlalchemy.orm import Session
from bot.handlers.command_interface import CommandsInterface
from bot.logger import get_logger


from bot.user.models.user import User


class GetInfoHandler(CommandsInterface):

    def __init__(self, session: Session):
        super().__init__(session)

    def handle(self, user: User):
        self.get_reply_message_data()

    def get_reply_message_data(self):
        get_logger.info("Это команда info")
        return {
            "text": self._get_text_message(),
            "keyboard": self._get_reply_keyboards(),
            "parse_mode": self._get_parse_mode(),
        }

    def _get_text_message(self) -> str:
        return "Это информация о боте."

    def _get_reply_keyboards(self):
        return None

    def _get_parse_mode(self) -> str:
        return "Markdown"