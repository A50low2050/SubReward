from abc import ABC, abstractmethod
from telegram import Message
from typing import Any


class IValidator(ABC):
    """Абстрактный базовый класс для всех валидаторов"""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Абстрактный метод для валидации данных.

        Args:
            data: Данные для валидации
        """
        pass


class MessageValidator(IValidator):
    """Класс для валидации сообщений"""

    def validate(self, message: Message | None) -> bool:
        """
        Валидирует сообщение и решает, нужно ли его обрабатывать

        Args:
            message: Объект сообщения для валидации

        """

        if message is None:
            raise ValueError("Параметр message не может быть пустым")

        if message.text is None:
            raise ValueError("Текст не должен быть пустым")

        return True

validator = MessageValidator()