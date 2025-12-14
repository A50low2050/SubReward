from api_client.TelegramBotRequest import TelegramBotRequest
from api_client.request_factory_interface import RequestInterface


class TelegramBotRequestFactory:
    @staticmethod
    def create_user(payload) -> RequestInterface:
        return TelegramBotRequest("POST", "/user/create", payload)

    @staticmethod
    def update_user(payload) -> RequestInterface:
        return TelegramBotRequest("POST", "/user/update", payload)

    @staticmethod
    def update_user_status(payload) -> RequestInterface:
        return TelegramBotRequest("POST", "/user/update-status", payload)

    @staticmethod
    def get_user(payload) -> RequestInterface:
        return TelegramBotRequest("GET", "/user/get/", payload)

    @staticmethod
    def get_none_subscribed_users(payload) -> RequestInterface:
        return TelegramBotRequest("GET", "/user/non_subscribed_users", payload)

    @staticmethod
    def get_users_gift(payload) -> RequestInterface:
        return TelegramBotRequest("GET", "/user/gift", payload)


# class GetUsersGiftInterface(RequestInterface):
#     def create_request(self, payload: Any = None) -> ApiRequest:
#         return ApiRequest("GET", "/user/gift")
