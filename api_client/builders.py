from typing import Dict, Any
from api_client.TelegramBotRequest import TelegramBotRequest


class TelegramBotRequestBuilder:
    def __init__(self):
        self._method = None
        self._endpoint = None
        self._data: Dict[str, Any] = {}

    def set_method(self, method: str):
        self._method = method.upper()
        return self

    def set_endpoint(self, endpoint: str):
        self._endpoint = endpoint
        return self

    def add_param(self, key: str, value: Any):
        self._data[key] = value
        return self

    def set_data(self, data: Dict[str, Any]):
        self._data = data
        return self

    def build(self):
        if not self._method:
            raise ValueError("Метод запроса не установлен")
        if not self._endpoint:
            raise ValueError("Endpoint не установлен")

        return TelegramBotRequest(
            method=self._method,
            endpoint=self._endpoint,
            data=self._data
        )
