import httpx
from typing import Dict, Any
from bot.models.user import User
from utils.apiclient import ApiClient
from utils.factories.request_factory import RequestFactory



class ApiService:
    def __init__(self):
        self.api_url = "http://demo3.sitewill.ru/api/telegram"

    def _new_connection(self) -> ApiClient:
        return ApiService(self.api_url)


    async def send_request(self, factory: RequestFactory, payload=None) -> httpx.Response:
        request = factory.create_request(payload)
        api = self._new_connection()
        try:
            response = getattr(api, request.method.lower())(
                request.endpoint,
                data=request.data
            )
            print(f"Ответ сервера ({request.method} {request.endpoint}): {response}")
            return response
        finally:
            api.close()

    async def update_user(self, user: User) -> httpx.Response:
        """Обновляет данные пользователя."""
        try:
            response = await self._send_request(
                "PATCH",  # Исправлено на PATCH для соответствия REST
                "/user/update",
                user.to_dict()
            )

            if response.status_code == 404:
                print(f"Пользователь {user.id} не найден")
            elif response.status_code == 400:
                print(f"Некорректные данные: {response.json().get('errors', '')}")

            return response

        except httpx.HTTPError as e:
            print(f"Ошибка при обновлении пользователя {user.id}: {e}")
            raise

    async def new_member(self, user: User) -> httpx.Response:
        """Регистрирует нового пользователя."""
        try:
            return await self._send_request(
                "POST",
                "/user/create",
                user.to_dict()
            )
        except httpx.HTTPError as e:
            print(f"Ошибка при создании пользователя {user.id}: {e}")
            raise

    async def send_status(self, post_data: Dict[str, Any])-> httpx.Response:
        """Отправляет статус пользователя на сервер."""
        try:
            response = await self._send_request(
                "POST",
                "/user/update-status",
                post_data
            )

            if response.status_code == 400:
                print("Некорректные данные:", response.json().get('error'))

            return response

        except httpx.HTTPError as e:
            print(f"Ошибка при отправке статуса: {e}")
            raise

    async def get_member(self, params: Dict[str, Any] = None) -> Dict[str, Any]:
        try:
            response = await self._send_request(
                "GET",
                "/user/get/",
                params=params or {}
            )

            if response.status_code == 404:
                print("Пользователь не найден")
                return {}

            return response.json()

        except httpx.HTTPError as e:
            print(f"Ошибка при получении пользователя: {e}")
            raise

    async def get_non_subscribed_users(self) -> Dict[str, Any]:
        try:
            response = await self._send_request(
                "GET",
                "/user/non_subscribed_users"
            )
            print(f"Получено {len(response.json())} пользователей без подписки")
            return response.json()
        except httpx.HTTPError as e:
            print(f"Ошибка при получении пользователей без подписки: {e}")
            raise

    async def get_users_gift(self) -> Dict[str, Any]:
        try:
            response = await self._send_request(
                "GET",
                "/user/gift"
            )
            gift_data = response.json()
            print(f"Получено {len(gift_data.get('users', []))} пользователей с подарками")
            return gift_data
        except httpx.HTTPError as e:
            print(f"Ошибка при получении пользователей с подарками: {e}")
            raise
