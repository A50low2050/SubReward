from abc import ABC, abstractmethod
from bot.user.domain.entities.user import User

class RegistrationStrategy(ABC):
    @abstractmethod
    def register(self, user_data: dict) -> User:
        pass

class GuestRegistrationStrategy(RegistrationStrategy):
    def register(self, user_data: dict) -> User:
        user_data['group_name'] = 'guest'
        return User.create(**user_data)

class MatrixRegistrationStrategy(RegistrationStrategy):
    def register(self, user_data: dict) -> User:
        user_data['group_name'] = 'matrix'
        return User.create(**user_data)
