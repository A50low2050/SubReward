from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from datetime import datetime

class ResponseInterface(ABC):
    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def get_error(self) -> str:
        pass

    @abstractmethod
    def get_data(self) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def date_created_at(self) -> datetime:
        pass
