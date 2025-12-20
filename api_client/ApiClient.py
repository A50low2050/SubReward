import httpx

from api_client.builders import TelegramBotRequestBuilder
from bot.models.user import User
from utils.apiclient import ApiClient
from api_client.request_factory_interface import RequestInterface


class ApiService:
    def __init__(self):
        self.api_url = "http://demo3.sitewill.ru/api/telegram"

    def _new_connection(self) -> ApiClient:
        return ApiClient(self.api_url)

    async def send_request(self, request: RequestInterface) -> httpx.Response:
        match request.get_method():
            case "POST":
                return self.post(request)
            case "GET":
                return self.get(request)
            case _:
                return "Неизвестный тип"


    def post(self, request):
        api = self._new_connection()
        try:
            return api.post(request.get_endpoint(), request.get_payload())
        except httpx.HTTPError as e:
            print(f"Ошибка при обновлении пользователя {request}:{e}")
            raise
        finally:
            api.close()

    def get(self, request):
        api = self._new_connection()
        return api.get(request.get_endpoint(), request.get_payload())

    async def get_users_gift(self):
        return {}

    async def update_user(self, user: User):
        return user

    async def new_member(self, user: User):
        return user
