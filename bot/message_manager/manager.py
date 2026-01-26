from telegram import Update, Message
from telegram.ext import ContextTypes
from .converter import MessageConverter
from ..handlers.command_interface import CommandsInterface
from ..handlers.handler_factory import HandlerFactory
from bot.processor.handler_processor import ProcessMessageManager
from .models import MessageInputDTO
from .validators import validator
from bot.logger import get_logger
from ..user.application.services.user_manager import UserManager
from bot.database.session import session_scope
from ..user.infra.repositories.user_repository_impl import UserRepository




class ManagerMessage:
    def input_message(self, message: Message) -> MessageInputDTO | bool:
        is_valid = validator.validate(message)

        if not is_valid:
            return is_valid

        return MessageConverter.convert(message)

    async def output_message(self, update: Update, command: CommandsInterface):
        data = command.get_reply_message_data()
        await update.message.reply_text(
            data.get("text"),
            reply_markup=data.get("keyboard"),
            parse_mode=data.get("parse_mode"))

async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message_manager = ManagerMessage()
    message_converter = MessageConverter()

    with session_scope() as session:
        user_repository = UserRepository(session)
        user_manager = UserManager(message_converter, user_repository)
        handler_factory = HandlerFactory(session)
        processor_manager = ProcessMessageManager(handler_factory)

        try:
            msg_dto = message_manager.input_message(update.message)
            user = user_manager.handle_new_message(update.message)
            handler = processor_manager.process(msg_dto, user)
            await message_manager.output_message(update, handler)
            get_logger.info(f"Сообщение: {msg_dto}")
        except ValueError as error:
            get_logger.error(error)
            raise error
