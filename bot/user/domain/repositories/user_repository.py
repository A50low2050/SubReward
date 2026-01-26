from abc import ABC, abstractmethod
from bot.user.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass