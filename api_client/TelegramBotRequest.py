from typing import Dict, Any
from api_client.request_factory_interface import RequestInterface


class TelegramBotRequest(RequestInterface):

    def __init__(self, method: str, endpoint: str, data: Dict[str, Any]):
        self.method = method
        self.endpoint = endpoint
        self.data = data


    def get_method(self) -> str:
        return self.method

    def get_endpoint(self) -> str:
        return self.endpoint

    def get_payload(self) -> Dict[str, Any]:
        return self.data