import httpx
from typing import Dict, Any
from utils.apiclient import ApiClient


class ApiService:
    def __init__(self):
        self.api_url = "https://api.sitewill.ru"

    def _new_connection(self) -> ApiClient:
        return ApiClient(self.api_url)

    async def new_member(self, post_data: Dict[str, Any]):
        api = self._new_connection()
        try:
            # Выполняем POST-запрос
            response = api.post("/api/member/add/", data=post_data)
            print("Ответ на POST-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()

    async def get_member(self) -> Dict[str, Any]:
        api = self._new_connection()

        try:
            # Выполняем GET-запрос
            response = api.get("/api/member/get/", params={"key": "value"})
            print("Ответ на GET-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()
