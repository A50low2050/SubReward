from typing import Optional


class ApiRequestException(Exception):
    def __init__(self, error_status: int, error_message: str, name_endpoint: str, payload: Optional[dict] = None):
        self.error_status = error_status
        self.error_message = error_message
        self.name_endpoint = name_endpoint
        self.payload = payload or {}


    def _build_message(self) -> str:
        payload_str = ", ".join(f"{key}={value}" for key, value in self.payload.items())
        return (
            f"[{self.error_status}] {self.error_message} "
            f"(endpoint: {self.name_endpoint}, payload: {payload_str})"
        )

    def __str__(self) -> str:
        return self._build_message()
