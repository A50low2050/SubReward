from sqlalchemy.orm import Session
from bot.handlers.command_interface import CommandsInterface
from bot.logger import get_logger
from bot.message_manager.models import MessageInputDTO
from bot.user.models.user import User


class GetReferral(CommandsInterface):

    def __init__(self, session: Session):
        super().__init__(session)

    def handle(self, msg_dto: MessageInputDTO):
        self.get_reply_message_data()

    def get_reply_message_data(self):
        get_logger.info("Это команда referral")

        return {
            "text": self._get_text_message(),
            "parse_mode": self._get_parse_mode(),
        }

    def _get_text_message(self) -> str:
        return """ Это ваша реферальная ссылка """

    def _get_reply_keyboards(self):
        pass

    def _get_parse_mode(self) -> str:
        return "Markdown"