from abc import abstractmethod
from bot.message_manager.models import MessageInputDTO
from bot.message_manager.output_message_interface import OutputMessageInterface


class CommandsInterface(OutputMessageInterface):

    @abstractmethod
    def handle(self, dto: MessageInputDTO):
        pass

