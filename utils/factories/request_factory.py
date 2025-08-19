from abc import ABC, abstractmethod
from typing import Any
from config.settings import ApiRequest


class RequestFactory(ABC):
    @abstractmethod
    def create_request(self, payload: Any = None) -> ApiRequest:
        pass
