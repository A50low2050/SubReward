from abc import ABC, abstractmethod
from typing import Any, Dict


class RequestInterface(ABC):
    @abstractmethod
    def get_method(self) -> str:
        pass

    @abstractmethod
    def get_endpoint(self) -> str:
        pass

    @abstractmethod
    def get_payload(self) -> Dict[str, Any]:
        pass
