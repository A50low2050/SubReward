import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.groups.manager_group import ManagerGroup
from bot.handlers.command_interface import CommandsInterface
from bot.logger import get_logger
from bot.message_manager.models import MessageInputDTO
from bot.user.models.user import User
from bot.user.user_manager import UserManager


class StartHandler(CommandsInterface):


    def handle(self, msg_dto: MessageInputDTO):
        ManagerGroup().add_to_start(msg_dto.user)
        UserManager().check_and_register_user(msg_dto.user)
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
