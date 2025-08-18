import httpx
from typing import Dict, Any, Optional
from bot.models.user import User
from utils.apiclient import ApiClient


class ApiService:
    def __init__(self):
        self.api_url = "http://demo3.sitewill.ru/api/telegram"

    def _new_connection(self) -> ApiClient:
        return ApiClient(self.api_url)

    async def _send_request(
            self,
            method: str,
            endpoint: str,
            data: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """
            Общий метод для отправки HTTP-запросов.

            Args:
                method: HTTP-метод ("GET", "POST", "PATCH", etc.)
                endpoint: API endpoint (например, "/user/create")
                data: Данные для отправки

            Returns:
                Response от сервера

            Raises:
                httpx.HTTPError: Если произошла ошибка запроса
        """
        api = self._new_connection()
        try:
            response = getattr(api, method.lower())(endpoint, data=data)
            print(f"Ответ сервера ({method} {endpoint}):", response)
            return response
        finally:
            api.close()

    async def update_user(self, user: User):

        update_data = user.to_dict()
        api = self._new_connection()

        try:
            # Выполняем PATCH-запрос
            response = api.post("/user/update", data=update_data)

            print(f"Ответ сервера на обновление пользователя {user.id}:", response)

            if response.status_code == 404:
                print(f"Пользователь {user.id} не найден")
            elif response.status_code == 400:
                print(f"Некорректные данные: {response.json().get('errors', '')}")

            return response

        except httpx.HTTPError as e:
            print(f"Ошибка при обновлении пользователя {user.id}: {e}")
            raise  # Можно обработать ошибку по-другому, если нужно

        finally:
            api.close()

    # async def new_member(self, user:User):
    #     post_data = user.to_dict()
    #     api = self._new_connection()
    #     try:
    #         # Выполняем POST-запрос
    #         response = api.post("/user/create", data=post_data)
    #         print("Ответ на POST-запрос:", response)
    #         return response
    #     except httpx.HTTPError as e:
    #         print(f"Произошла ошибка при запросе: {e}")
    #
    #     finally:
    #         api.close()

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

    async def send_stuts(self, post_data: Dict[str, Any]):

        api = self._new_connection()
        try:
            # Выполняем POST-запрос
            response = api.post("/user/update-status", data=post_data)
            print("Ответ на POST-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()

    async def get_member(self) -> Dict[str, Any]:
        api = self._new_connection()

        try:
            response = api.get("/user/get/", params={"key": "value"})
            print("Ответ на GET-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()

    async def get_non_subscribed_users(self) -> Dict[str, Any]:
        print('Запрос')
        api = self._new_connection()

        try:
            response = api.get("/user/non_subscribed_users")
            print("Ответ на GET-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()

    async def get_users_gift(self) -> Dict[str, Any]:
        print('Запрос')
        api = self._new_connection()

        try:
            response = api.get("/user/gift")
            print("Ответ на GET-запрос:", response)
            return response
        except httpx.HTTPError as e:
            print(f"Произошла ошибка при запросе: {e}")

        finally:
            api.close()
