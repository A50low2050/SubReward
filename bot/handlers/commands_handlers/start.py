from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy.orm import Session
from bot.handlers.command_interface import CommandsInterface
from bot.logger import get_logger


from bot.user.domain.entities.user import User


class StartHandler(CommandsInterface):

    def __init__(self, session: Session):
        super().__init__(session)

    def handle(self, user: User):
        self.get_reply_message_data()

    def get_reply_message_data(self):
        get_logger.info("Это команда start")

        return {
            "text": self._get_text_message(),
            "keyboard": self._get_reply_keyboards(),
            "parse_mode": self._get_parse_mode(),
        }

    def _get_text_message(self) -> str:
        return """ Добро пожаловать в BeautyServiceBot! """

    def _get_reply_keyboards(self) -> InlineKeyboardMarkup:
        keyboard = [
            [
                InlineKeyboardButton("О нас  🔨", callback_data="get_info"),
            ],
        ]

        return InlineKeyboardMarkup(keyboard)

    def _get_parse_mode(self) -> str:
        return "Markdown"
