from telegram import Update, Message
from telegram.ext import ContextTypes
from .converter import MessageConverter
from .output_message_interface import OutputMessageInterface
from ..handlers.command_interface import CommandsInterface
from ..handlers.handler_factory import HandlerFactory
from bot.processor.handler_processor import ProcessMessageManager
from .models import MessageInputDTO
from .validators import validator
from bot.logger import get_logger
from bot.database.session import session_scope
from bot.user.repositories.user_repository import UserRepository
from bot.user.services.user_service import UserService




class ManagerMessage:
    def input_message(self, message: Message) -> MessageInputDTO | bool:
        is_valid = validator.validate(message)

        if not is_valid:
            return is_valid

        return MessageConverter.convert(message)

    async def output_message(self, update: Update, output_message: OutputMessageInterface):
        data = output_message.get_reply_message_data()
        await update.message.reply_text(
            data.get("text"),
            reply_markup=data.get("keyboard"),
            parse_mode=data.get("parse_mode"))

async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        message_manager = ManagerMessage()

        # user_repository = UserRepository()
        user_service = UserService()

        handler_factory = HandlerFactory()
        processor_manager = ProcessMessageManager(handler_factory)

        msg_dto = message_manager.input_message(update.message)
        print(msg_dto)
        # user = user_service.register_user(msg_dto)

        handler = processor_manager.process(msg_dto)

        await message_manager.output_message(update, handler)
        get_logger.info(f"Сообщение: {msg_dto}")
    except ValueError as error:
        get_logger.error(error)
        raise error
