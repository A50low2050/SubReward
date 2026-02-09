from bot.handlers.command_interface import CommandsInterface
from bot.handlers.commands_handlers.get_info import GetInfoHandler
from bot.handlers.commands_handlers.get_ref import GetReferral
from bot.handlers.commands_handlers.start import StartHandler
from bot.logger import get_logger


class HandlerFactory:

    _handlers = {
        "start": StartHandler,
        "get_info": GetInfoHandler,
        "get_referral": GetReferral,
    }


    def get_handler(self, command_name: str) -> CommandsInterface:

        if command_name not in self._handlers:
            get_logger.error(f"Нет обработчиков для команды {command_name}")

        handler_class = self._handlers.get(command_name)

        return handler_class()



