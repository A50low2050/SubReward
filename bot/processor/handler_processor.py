from bot.handlers.command_interface import CommandsInterface
from bot.handlers.handler_factory import HandlerFactory
from bot.logger import get_logger
from bot.message_manager.models import MessageInputDTO
from bot.user.domain.entities.user import User


class ProcessMessageManager:

    def __init__(self, factory: HandlerFactory):
        self.factory = factory

    def process(self, dto: MessageInputDTO, user: User) -> CommandsInterface:

        if dto.type == 'command':
            handler = self.factory.get_handler(dto.command)
            handler.handle(user)
            return handler

        else:
            get_logger.info("Это текстовое сообщение")
