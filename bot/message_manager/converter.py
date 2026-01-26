from telegram import Message

from bot.message_manager.models import MessageInputDTO


class MessageConverter:
    # type_message = {
    #     "/": "command",
    #     "": "text",
    # }

    @classmethod
    def convert(cls, message: Message) -> MessageInputDTO:

        return MessageInputDTO(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username,
            message_id=message.message_id,
            chat_id=message.chat_id,
            text=message.text,
            type=cls._determine_message_type(message.text),
            command=cls._get_command(message.text),
        )

    @staticmethod
    def _determine_message_type(message_text: str) -> str:
        if message_text and message_text.startswith('/'):
            return "command"
        elif message_text:
            return "text"

    @staticmethod
    def _get_command(message_text: str) -> str | None:
        if message_text.startswith('/'):
            return message_text.replace('/', '')
        return None