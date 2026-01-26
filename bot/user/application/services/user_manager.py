from telegram import Message
from bot.message_manager.manager import MessageConverter
from bot.user.domain.entities.user import User
from bot.user.infra.repositories.user_repository_impl import UserRepository
from bot.user.application.services.registration_strategy_factory import RegistrationStrategyFactory


class UserManager:

    def __init__(self, message_converter: MessageConverter, user_repository: UserRepository):
        self.message_converter = message_converter
        self.user_repository = user_repository

    def handle_new_message(self, message: Message) -> User:

        message_dto = self.message_converter.convert(message)

        user_data = {
            'id': message_dto.user_id,
            'first_name': message_dto.first_name,
            'username': message_dto.username,
        }

        strategy = RegistrationStrategyFactory.get_strategy(message.text)
        user = strategy.register(user_data)

        return self.user_repository.save(user)