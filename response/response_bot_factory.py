from typing import Any, Dict, Optional
from datetime import datetime
from exception.api_request_exception import ApiRequestException
from response.response_factory_interface import ResponseInterface


class Response(ResponseInterface):
    def __init__(
            self,
            status: int,
            error: str,
            data:Optional[Dict[str, Any]],
            endpoint: str,
            payload: Optional[dict] = None
    ):
        self._status = status
        self._error = error
        self._data = data
        self._date_created_at = datetime.now()
        self._endpoint = endpoint
        self._payload = payload or {}

    def get_status(self) -> int:
        if self._status == 400:
            raise ApiRequestException(
                error_status=self._status,
                error_message=self._error or "Unknown error",
                name_endpoint=self._endpoint,
                payload=self._payload
            )
        return self._status

    def get_error(self) -> Optional[str]:
        return self._error

    def get_data(self) -> Optional[Dict[str, Any]]:
        return self._data

    def get_date_created_at(self) -> datetime:
        return self._date_created_at

    def is_success(self) -> bool:
        return self._status == "success"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "error": self._error,
            "data": self._data,
            "date_created_at": self._date_created_at.isoformat()
        }
